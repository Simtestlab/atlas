# Issue #1: Requirement Documentation

**Repository:** ecal_backend  
**Status:** Open  
**Created:** 2024-12-31  
**Updated:** 2025-01-11  
**Author:** @harish-ramar  
**Assignees:** @harish-ramar  

[View on GitHub](https://github.com/Simtestlab/ecal_backend/issues/1)

## Description

# eCal Documentation

This the Yggdrasil backend project. Running a [Node.js](https://nodejs.org/en) express app to expose a [REST](https://restfulapi.net/)
API for calibration data management.

To install first clone the git repo `git clone git@gitlab.infimotion.com:valhalla/docker/services/yggdrasil-backend.git`

## Introduction

Calibration of an embedded software is the process of applying values to *global variables* after the software has been
compiled into an executable binary.

The build process can be summarized as follows:

```plantuml
file ".c/.h" as code
file ".dcm" as dcm
file ".a2l" as a2l
file ".hex" as hex

code --> (Compile Code)
(Compile Code) -> (Link Executable) : ".o/.obj"
(Link Executable) -> (Convert Hex) : ".elf"
(Convert Hex) -> (Calibrate Executable) : ".cal.hex"

a2l --> (Calibrate Executable)
dcm --> (Calibrate Executable)

(Calibrate Executable) -> hex
```

1. Code is compilds into object files (or libraries)
1. Objects and/or libraries are linked to an executable in ELF format.
1. The ELF file is converted to intel or motorola HEX format.
1. Calibration is applied using *DCM* files (data) and *A2L* files (data descriptors)

The global variables are declared with their properties (name and data type) globally for the executable, hence the name must
be unique to avoid linking errors. An example by pseudo code:

```
#include "Rte_Type.h"

...

volatile boolean C_disableThrottle = FALSE;

...

RTE_RETVAL engageThrottle(...) {

... 

    if (C_disableThrottle == TRUE) {
        // Debug software
    } else {
        // Prod
    }

    return 0u;
}
```

`C_disableThrottle` is declared in the compilation unit globally. The keyword `volatile` is needed so the compiler does not
remove the *"symbol"* `C_disableThrottle` as this will be used to set it's actual value after the executable is produced.

The calibration process will set the value accordingly using the actual value in a `.dcm` file (here 0 or 1). Also to be able to
know where in the memory this global variable has been placed, the `.a2l` file must be provided where this information exists.

See the [ASAM MCD-2 MC](https://www.asam.net/standards/detail/mcd-2-mc/) for further details of `.a2l` files and 
[DCM file formats](https://www.etas.com/en/downloadcenter/2582.php) for more information about the specifics of the *DCM* file
formats.

## Requirements

### Database

1. RDB supporting [tree structures](https://www.baeldung.com/cs/storing-tree-in-rdb). [PostgreSQL](https://www.postgresql.org/) v16 is preferred
1. Database deployment shall support redundancy layering, e.g. backup/syncrhonize
1. Database tables shall support a folder based structure \
    ```
    Base - Can be company/department, etc (top node)
    ├───ProjectX (branch)
    │   ├───Component (leaf)
    │   └───Sub-project/Variant (branch)
    │       └───Component (leaf)
    └───ProjectY...
    ```
    1. Base project shall only link to one or more project tables.
    1. Project shall be able to link to sub-project(s) and component tables.
    1. Components shall contain the calibration data only.
1. Base project names must be unique on root level.
1. Project(s) and component(s) names must be unique under their base.
1. Component tables shall store calibration data (a.k.a *characteristic*) in DCM format version 2 compatible way. The following datatypes shall be supported:
    1. Parameter
    ```
    FESTWERT <name>
        LANGNAME "<comment text>"
        DISPLAYNAME <name>
        VAR <name>=<value>
        FUNKTION <name>
        EINHEIT_W "<unit text>"
        WERT <value>
    END
    ```
    2. Enum
    ```
    FESTWERT <name>
        TEXT <text>
    END
    ```
    3. Text
    ```
    TEXTSTRING <name>
        FUNKTION <name>
        LANGNAME <"comment text">
        TEXT   "text"
    END
    ```
    4. Array
    ```
    FESTWERTEBLOCK <name> <size_x>
        LANGNAME "<comment text>"
        DISPLAYNAME <name>
        FUNKTION <name>
        EINHEIT_W "<unit text>"
        WERT <value list> // list size has to be equal to size_x
    END
    ```
    5. Matrix
    ```
    FESTWERTEBLOCK <name> <size_x> @ <size_y>
        LANGNAME "<comment text>"
        FUNKTION <name>
        EINHEIT_W "<unit text>"
        WERT <value list> // list size has to be equal to size_x
        WERT ...          // number of list has to be equal to size_y
    END
    ```
    6. Line
    ```
    KENNLINIE <name> <size_x>
        LANGNAME "<comment text>"
        FUNKTION <name>
        EINHEIT_X "<unit text>"
        EINHEIT_W "<unit text>"
        ST/X <X sample point list> // sample points list size has to be equal to size_x
        WERT <value list> // list size has to be equal to size_x
    END
    ```
    7. Map
    ```
    KENNFELD <name> <size_x> <size_y>
        FUNKTION <name>
        EINHEIT_X "<unit text>"
        EINHEIT_Y "<unit text>"
        EINHEIT_W "<unit text>"
        ST/X <X sample point list> // sample points list size has to be equal to size_x
        ST/Y <Y sample point> // element contains size_y pairs of ST/Y and WERT lines
        WERT <value list> // list contains size_x values
        ST/Y ...
        WERT ...
    END
    ```
    8. Fixed line
    ```
    FESTKENNLINIE <name> <size_x> // Same as line
        LANGNAME "<comment text>"
        EINHEIT_X "<unit text>"
        EINHEIT_W "<unit text>"
        ST/X <X sample point list>
        WERT <value list>
    END
    ```
    9. Fixed map
    ```
    FESTKENNFELD <name> <size_x> <size_y> // Same as map
        LANGNAME "<comment text>"
        EINHEIT_X "<unit text>"
        EINHEIT_Y "<unit text>"
        EINHEIT_W "<unit text>"
        ST/X <X sample point list>
        ST/Y <Y sample point>
        WERT <value list>
        ST/Y ...
        WERT ...
    END
    ```
    10. Group line
    ```
    GRUPPENKENNLINIE <name> <size_x>
        LANGNAME "<comment text>"
        EINHEIT_X "<unit text>"
        EINHEIT_W "<unit text>"
        *SSTX <X distribution>
            ST/X <X sample point list> // sample points list size has to be equal to size_x
            WERT <value list> // list size has to be equal to size_x
    END
    ```
    11. Group map
    ```
    GRUPPENKENNFELD <name> <size_x> <size_y>
        LANGNAME "<comment text>"
        EINHEIT_X "<text>"
        EINHEIT_Y "<text>"
        EINHEIT_W "<unit text>"
        *SSTX <X distribution> 
        *SSTY <Y distribution>
            ST/X <X sample point list> // sample points list size has to be equal to size_x
            ST/Y <Y sample point> // element contains size_y pairs of ST/Y and WERT lines
            WERT <value list> // list contains size_x values
            ST/Y ...
            WERT ...
    END
    ```
    12. Distribution
    ```
    STUETZSTELLENVERTEILUNG <name> <size_x>
        LANGNAME "<comment text>"
        EINHEIT_X "<text>"
        ST/X <sample point list> // list contains size_x values
    END
    ```
1. Project(s) shall be version controlled.
    1. The project have a main *baseline*, with the name *main*.
    1. It shall be possible to *freeze* a baseline. All data becomes read-only and possibility to jump to this label later.
    1. Freeze labels shall be unique per project.
    1. Modifications shall be done in *working sets*, e.g. *branches*.
    1. Working sets shall be able to be merged to the baseline/main.
    1. Conflicts shall be detected and an error code emitted if so.

> **Explanations**
>
> - `<value>` is the value of a scalar parameter. The type depends on the setting for the element, it can be float, signed integer, or unsigned integer.
> - `<name>` and `<something text>` is a string represeted in UTF-8 textual format.
> - `<value list>` is a list of values from a one- or two-dimensional parameter (array, matrix, characteristic line/map). The type depends on the setting for the element, it can be float, signed integer, or unsigned integer, or logical (array and matrix only).
> - `<size_x>` and `<size_y>` are the **X** and **Y** size of the element, represented by unsigned integers.
> - `<X sample point list>` is a list of **X** sample points of a characteristic line or map, or a dsitribution. The type depends on the setting for the element, it can be float, signed integer, or unsigned integer.
> - `<Y sample point>` is an **Y** sample point of a characteristic map. The type depends on the setting for the element, it can be float, signed integer, or unsigned integer.
> - `<X distribution>` and `<Y distribution>` are the names of the distributions used in group characteristic lines and maps.

### Backend

1. Base platform shall be *Node.js* with *express* as a web app.
1. Backend provides a *RESTful* API
    1. Protected endpoints using *AA* (authentication and authorization) and input validation (e.g. *express-validator*)
    1. OpenAPI documentation with [swagger](https://swagger.io/specification/)
    1. The API shall honor the *CRUD* pattern
    1. The API shall respond the client with proper [HTTP response codes](https://restfulapi.net/http-status-codes/)
1. Dockerized setup compatible with [Valhalla software factory](https://valhalla.infimotion.com)
    1. Dev environment for testing
    1. Prod environment for using

### User management

1. Authentication using LDAP
1. Roles:
    1. Developer (default), can create, edit and remove components.
    1. Reader, can only view and export data.
    1. Manager, same as developer but also grants permission for users on project and can create new projects or components.
    1. Bot, machine account, shall be allowed to use the REST API.
    1. Admin, superuser, all of the above and management of users.
1. Authorization shall be set on base and project folders. Inheritance based.
1. It shall be possibile to create groups where users can be a member of.

### DCM import and export

1. The backend shall provide an API to export all calibration data from a project and download as a DCM file.
1. The backend shall provide an API to import all calibration data from a DCM file into a project.
1. Import of a DCM file shall be possible on project level.
    1. Each entry in the DCM file to be parsed and added to a new component if it does not already exist.
    1. The import API shall be configurable, e.g. by providing the following parameters if component already exist.
        1. Skip. Skip importing the component and continue with the next one.
        1. Overwrite. Import the component and completely overwrite existing one.
        1. Cancel. Skip importing and abort operation. This requires that a pre-import needs to be done to check all components.

### Quality assurance

1. Unit tests using chai or similar approach.

## Architecture

The backend project shall follow an [MVC](https://en.wikipedia.org/wiki/Model-view-controller) pattern approach.

* The *Model* represents the database interactions, and business logic of the application. It is responsible for implementing the \
 core business rules and application logic and also focuses on *CRUD* operations, data validation, and maintaining data integrity.
* The *View* primary responsibility is to present the data to the user via an RESTful API. It receives data from the Model via \
 Controllers and renders it for the user to interact with.
* Controller serves as an intermediary component that receives user input, updates the Model data as needed, and coordinates the \
 interaction between the Model and the View. The Controller updates the Model based on user input.
 
### Project structure

The project structure shall honor the MVC pattern and provide the implementation into the following folders:

```
├───newsfragments           # Used in CI and release process to autogenerate changelog, see python town-crier tool.
├───nginx                   # Nginx reverse proxy serving connectivity using SSL
├───tests                   # Unit tests for the backend
└───yggdrasil-backend
    ├───config              # Configuration files
    ├───controllers         # Implements the business logic
    ├───middleware          # Third party functionality, e.g. for authentication and authorization.
    ├───models              # Represents database models 
    ├───routes              # Represents the view and provides the API as specified by the [openapi.yaml](openapi.yaml) file.
    └───services            # Utility functions
```

### Database tables

#### Users

This table contains the username with the following fields and datatypes.

| Id (pk) | Username (unique) | Role | Active | createdAt | updatedAt |
|:--------|:------------------|:-----|:-------|:----------|:----------|
|Integer  |String             |Enum  |Boolean |DateTime   |DateTime   |

- Id is an integer used as primary key.
- Username is a string honoring proper user name `firstname.lastname` in UTF-8 format. Must be unique.
- Role (Enumeration of Administrator, Manager, Developer and Reader)
- Active (Boolean). Set as default to `false` upon user registration. Only activated users are authorized to login.

An optional field for password could be added for local authentication if not using LDAP.

#### Groups

This table contains group names with list of users

| Id (pk) | Groupname (unique) | Description | createdAt | updatedAt |
|:--------|:-------------------|:------------|:----------|:----------|
|Integer  |String              |String       |DateTime   |DateTime   |

- Id is an integer used as primary key.
- Groupname is a string defining the name of the group in UTF-8 format. Must be unique.
- Description is a free text field describing the group.

#### RootNodes

This table shall represent the root or base of a hierarchy.

| Name (pk) | Table ID | Access  | Projects | createdAt | updatedAt |
|:----------|:---------|:--------|:---------|:----------|:----------|
|String     |Integer   |String[] |Integer[] |DateTime   |DateTime   |

- Name (primary key). A unique name of the base.
- Table ID. A unique sequence number used to link child projects.
- Access. List of accesses. Can contain user names and group names.
- Projects. A list of project table IDs that belong under this root node.

#### ProjectNodes

This table represent project and sub-project nodes.

| Name (pk) | Table ID | Access  | Root   | Projects | Components | createdAt | updatedAt |
|:----------|:---------|:--------|:-------|:---------|:-----------|:----------|:----------|
|String     |Integer   |String[] |Integer |Integer[] |Integer[]   |DateTime   |DateTime   |

- Name (primary key). A unique name of the project.
- Table ID. A unique sequence number used to link sub projects.
- Access. List of accesses. Can contain user names and group names.
- Root. The Table ID of the root node. This is needed to retrieve access from parent if access is not set explicitly on the project.
- Projects. A list of project table IDs that belong under this project node.
- Components. A list of component table IDs that belong under this project node.

#### ComponentNodes

The following tables represent the *leaf* nodes of the structure which contain the actual calibration data.

#### ComponentNode

This table shall contain the name and sequence ID of any arbitry component. The purpose is to maintain uniqueness among all
components with regards to the name and component ID. For the following tables, the name, value ID and baseline shall be linked
with the component node table.

| Name (pk) | Value ID | Baseline (pk) | createdAt | updatedAt |
|:----------|:---------|:------------- |:----------|:----------|
|String     |Serial    |String         |DateTime   |DateTime   |

- Name (primary key). A unique name of the component.
- Value ID. A unique sequence number used to link sub projects.
- Baseline. A unique baseline name, default is *main*.

The name and baseline represents the primary key pair. E.g. It shall be possible to have several components with the same
name as long as the baseline is different.

#### ParameterNode

This table represents the parameter characteristic (`FESTWERT`).

| Name (pk) | Value ID | Baseline (pk) | Displayname | Description | Var   | Function | Unit  | Value | Text  | createdAt | updatedAt |
|:----------|:---------|:--------------|:----------- |:----------- |:------|:---------|:----- |:------|:------|:----------|:----------|
|String     |Serial    |String         |String       |String       |JSONB  |String    |String |Float  |String |DateTime   |DateTime   |

- Displayname. An optional display name if diffenent from name.
- Description. An optional description for this value.
- Var. An optional name value pair repsented with as a JSONB type.
- Function. An optional function name.
- Unit. An optional unit name.
- Value. The actual value represented in floating points.
- Text. Textual representation of the value.

*Value* and *Text* columns are mutually exclusive. The value is either a numerical or a textual. This applies to all other nodes as well.

#### TextNode

This table represent text strings (`TEXTSTRING`).

| Name (pk) | Value ID | Baseline (pk) | Displayname | Description | Function | Value | createdAt | updatedAt |
|:----------|:---------|:--------------|:------------|:------------|:---------|:------|:----------|:----------|
|String     |Serial    |String         |String       |String       |String    |String |DateTime   |DateTime   |

- Displayname. An optional display name if diffenent from name.
- Description. An optional description for this value.
- Function. An optional function name.
- Value. The actual value.

#### ArrayNode

This table represents an array of values (`FESTWERTEBLOCK`).

| Name (pk) | Value ID | Baseline (pk) | Displayname | Description | Function | Unit  | Values | Texts   | createdAt | updatedAt |
|:----------|:---------|:--------------|:------------|:------------|:---------|:------|:-------|:--------|:----------|:----------|
|String     |Serial    |String         |String       |String       |String    |String |Float[] |String[] |DateTime   |DateTime   |

- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the array.
- Function. An optional function name.
- Unit. An optional unit name.
- Values. The actual values.
- Texts. The textual representation of values.

#### MatrixNode

This table represents a matrix (`FESTWERTEBLOCK`).

| Name (pk) | Value ID | Baseline (pk) | Displayname | Description | Function | Unit  | Values   | Texts     | createdAt | updatedAt |
|:----------|:---------|:--------------|:------------|:----------- |:---------|:------|:---------|:----------|:----------|:----------|
|String     |Serial    |String         |String       |String       |String    |String |Float[][] |String[][] |DateTime   |DateTime   |

- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the matrix.
- Function. An optional function name.
- Unit. An optional unit name.
- Values. The actual values.
- Texts. The textual representation of values.

#### LineNode

This table represents a line. It can also be set to *"fixed"* according to the DCM standard, (`KENNLINIE` and `FESTKENNLINIE`).

| Name (pk) | Value ID | Baseline (pk) | Fixed  | Displayname | Description | Function | LineUnit | ValueUnit | SamplePoints | Values | Texts   | createdAt | updatedAt |
|:----------|:---------|:--------------|:-------|:------------|:------------|:---------|:---------|:----------|:-------------|:-------|:--------|:----------|:----------|
|String     |Serial    |String         |Boolean |String       |String       |String    |String    |String     |Float[]       |Float[] |String[] |DateTime   |DateTime   |

- Boolean. Set to true if this is a *fixed* line.
- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the line.
- Function. An optional function name.
- LineUnit. An optional unit name for the line.
- ValueUnit. An optional unit name for the values.
- SamplePoints. Line values, can be empty if line is fixed.
- Values. The actual values.
- Texts. The textual representation of values.

#### MapNode

This table represents a map (or curve). It can also be set to "fixed" according to the DCM standard  (`KENNFELD` and `FESTKENNFELD`).

| Name (pk) | Value ID | Baseline (pk) | Fixed  | Displayname | Description | Function | ValueUnitX | ValueUnitY | LineUnit | SamplePoints | Values   | Texts     | createdAt | updatedAt |
|:----------|:---------|:--------------|:-------|:------------|:------------|:---------|:-----------|:-----------|:---------|:-------------|:---------|:----------|:----------|:----------|
|String     |Serial    |String         |Boolean |String       |String       |String    |String      |String      |String    |Float[][]     |Float[][] |String[][] |DateTime   |DateTime   |

- Boolean. Set to true if this is a *fixed* map.
- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the map.
- Function. An optional function name.
- LineUnit. An optional unit name for the map.
- ValueUnitX. An optional unit name for the X-axis values.
- ValueUnitY. An optional unit name for the Y-axis values.
- SamplePoints. Map values, can be empty if map is fixed.
- Values. The actual values.
- Texts. The textual representation of values.

#### GroupLineNode

This table represents a group line (distribution). Essentially identical to **LineNode** but contains a label, (`GRUPPENKENNLINIE`).

| Name (pk) | Value ID | Baseline (pk) | Fixed  | Displayname | Description | Function | LineUnit | ValueUnit | Label | SamplePoints | Values | Texts   | createdAt | updatedAt |
|:----------|:---------|:--------------|:-------|:------------|:------------|:---------|:---------|:----------|:------|:-------------|:-------|:--------|:----------|:----------|
|String     |Serial    |String         |Boolean |String       |String       |String    |String    |String     |String |Float[]       |Float[] |String[] |DateTime   |DateTime   |

- Boolean. Set to true if this is a *fixed* line.
- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the line.
- Function. An optional function name.
- LineUnit. An optional unit name for the line.
- ValueUnit. An optional unit name for the values.
- Label. The distribution label.
- SamplePoints. Line values, can be empty if line is fixed.
- Values. The actual values.
- Texts. The textual representation of values.

#### GroupMapNode

This table represents a group map (distribution). Essentially identical to **MapNode** but contains labels for both distributions, (`GRUPPENKENNFELD`).

| Name (pk) | Value ID | Baseline (pk) | Fixed  | Displayname | Description | Function | ValueUnitX | ValueUnitY | LabelX | Label Y | LineUnit | SamplePoints | Values   | Texts     | createdAt | updatedAt |
|:----------|:---------|:--------------|:-------|:------------|:------------|:---------|:-----------|:-----------|:-------|:--------|:---------|:-------------|:---------|:----------|:----------|:----------|
|String     |Serial    |String         |Boolean |String       |String       |String    |String      |String      |String  |String   |String    |Float[][]     |Float[][] |String[][] |DateTime   |DateTime   |

- Boolean. Set to true if this is a *fixed* map.
- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the map.
- Function. An optional function name.
- LineUnit. An optional unit name for the map.
- ValueUnitX. An optional unit name for the X-axis values.
- ValueUnitY. An optional unit name for the Y-axis values.
- LabelX. The distribution label for the X-axis.
- LabelY. The distribution label for the Y-axis.
- SamplePoints. Map values, can be empty if map is fixed.
- Values. The actual values.
- Texts. The textual representation of values.

#### DistributionNode

This table represents distributions (`STUETZSTELLENVERTEILUNG`).

| Name (pk) | Value ID | Baseline (pk) | Displayname | Description | Function | Unit  | Values | Texts  | createdAt | updatedAt |
|:----------|:---------|:--------------|:------------|:------------|:---------|:------|:-------|:-------|:----------|:----------|
|String     |Serial    |String         |String       |String       |String    |String |Float[] |String  |DateTime   |DateTime   |

- Displayname. An optional display name if diffenent from name.
- Description. An optional description of the distribution.
- Function. An optional function name.
- Unit. An optional unit name for the distribution.
- Values. The actual values.
- Texts. The textual representation of values.

#### Relations

The following relations shall exist between tables.

```plantuml
!define primary_key(x) <b><color:#b8861b><&key></color> x</b>
!define foreign_key(x) <color:#aaaaaa><&key></color> x
!define column(x) <color:#efefef><&media-record></color> x
!define table(x) entity x << (T, white) >>

table(Users) {
  primary_key(id): UUID <<PK>>
  --
  column(username): VARCHAR(255) NOT NULL
  column(role): ENUM
  column(active): BOOLEAN
}

table(Groups) {
  primary_key(id): UUID <<PK>>
  --
  column(groupname): VARCHAR(255) NOT NULL
  column(description): VARCHAR(255) NOT NULL
}

table(UserGroup) {
  primary_key(id): UUID <<PK>>
  --
  foreign_key(groupId): UUID
  foreign_key(userId): UUID
}

Users }|--|{ Groups : has-many-belongs-to-many
Users ||--|| UserGroup : through
Groups ||--|| UserGroup : through

```


### Deployment

Deployment of the system shall be done using the [docker-compose.yml](docker-compose.yml) file which runs a basic
setup of the backend server itself, databases and an nginx reverse proxy serving SSL.

Administration of the database shall be possible directly using e.g. [PGAdmin](https://www.pgadmin.org/) tool.

```plantuml
actor "User"
actor "Developer"
actor "Admin"

node "Reverse Proxy Backend" {
  [Nginx]
}

node "Reverse Proxy Frontend" {
  [NginxWeb]
}

node "Frontend Server" {
  [WebApp]
}

node "Backend Server" {
  [Yggdrasil]
}

database "Database Server" {
  [PostgresSQL]
}

[User] <--> [NginxWeb] : http
[Developer] <-> [Nginx] : https
[WebApp] <-> [NginxWeb] : https
[WebApp] <--> [Nginx] : http
[Admin] <--> [PostgresSQL] : pgadmin
[Nginx] <--> [Yggdrasil] : http
[Yggdrasil] <-> [PostgresSQL] : http
```

## Development environment

A development environment is provided for conveniance. Use the [DevelopmentEnvironment.lnk](DevelopmentEnvironment.lnk)
file to start the environment. It will create a python virtual environment and also deploy the node virtual environment
in the same location which will be in your `%USERDIR\env\node_env`.

### NPM via nexus

You need to add _auth into `~/.npmrc`. Use `certutil -encode <inputfile> <outfile>` where inputfile contains your `username:password`.
Then copy the encoded credential into your `~./npmrc` file like this:

```
//valhalla.infimotion.com:8082/repository/npm-external/:_auth=YOUR_TOKEN
```

#### Update

Use `ncu -u` and `npm install` to update packages. For audit, use `npm audit fix --registry=https://registry.npmjs.org`.

### Run locally

* Make sure that you have _Node.js_ and _npm_ installed (done by the development environment script). If executing manually, _Node.js_ and _npm_ can be found [here](https://www.npmjs.com/get-npm).
* Make sure that you have PostgreSQL installed. If not, it can be found [here](https://www.postgresql.org/download/windows/). When asked for admin password, set it to `postgres`. Let the port be default: 5432.
* Create a new PostgreSQL database called `database_development`. This can be done either by using the command line tool (`psql`) or by using _pgAdmin_. _PgAdmin_ can be found [here](https://www.pgadmin.org/download/) or can be installed with PostgreSQL above as well.
* Create a new user: _"yggdrasil"_ with password _"foobar"_. Let this user be a _"superuser"_ as well.
* Navigate to the folder where you have Yggdrasil Backend cloned to.
* run `npm install` to install the package and dependencies.
* run `npm start` to start the package.
* Now you're ready to run Yggdrasil.

### Running tests

It's possible to test Yggdrasil Backend using the Swagger/OpenAPI documentation web page. Just open the following URL in your browser and change server to localhost: http://localhost:8080/api-docs. Click on one end point to expand it, and then click 'Try it out'. From here you can directly click 'Execute' or fill out any parameters
needed and then click *Execute*.

### Restore backed up data

Run `psql database_production yggdrasil < /dump/dump-20241126_101001.sql` on main Postgres container.

Change `dump-20241126_101001.sql` to the name of the file you want to restore from.

## Jenkins

### Daily Builds

Push to gitlab with the word _READY TO_ and _BUILD_, _TEST_ or _ANALYZE_ will start the
[daily build pipeline](https://valhalla.infimotion.com:8090/job/Software%20Tools/job/Docker%20Daily%20Build/). A successful build
is needed in order to merge your changes to master while a merge will deploy the development server.

### Nightly Builds

Any changes to master will trigger the [nightly build pipeline](https://valhalla.infimotion.com:8090/job/Software%20Tools/job/Docker%20Nightly%20Build/)
Only a trivy security analysis will be performed each night and if new vulnerabilities are found the nightly build fails and you should consider updating
to new packages in order to resolve the vulnerabilities.

### Release Builds

Upon pushing and merging a tag, the [relase build pipline](https://valhalla.infimotion.com:8090/job/Software%20Tools/job/Docker%20Release%20Build/)
will start. Just like the nightly build, upon success, the released version of the backend will be deployed to prod.

See below how to create a release tag.

## Release

Follow the guide in the [development environment](https://gitlab.infimotion.com/Valhalla/Environments/gugnir#Release_Strategy)
readme.
