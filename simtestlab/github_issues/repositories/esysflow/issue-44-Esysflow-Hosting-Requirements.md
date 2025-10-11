# Issue #44: Esysflow Hosting Requirements

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2024-12-05  
**Updated:** 2025-02-23  
**Closed:** 2025-02-23  
**Author:** @harish-ramar  
**Assignees:** @nallasivamselvaraj  
**Labels:** `documentation`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/44)

## Description

# Requirements for Esysflow:

Currently we doesn't require database, but in future we planned to implement **graph database** for that these are the database listen below. 

## Back End:
Esysflow uses **next.js** for it's back end system, **Next.js** is a react framework for creating back end system for react. So we need to ensure out hosting platform support **next.js**.

## Database:
In esysflow the data we store depends on graph database. From some refer along the I finalized two database platform which is best for storing **graph database**

- Arango DB. Link: https://arangodb.com/
- Neo4j. Link: https://neo4j.com/product/neo4j-graph-database/

### Advantages of ArangoDB:
-  Supports multi-model database for combining graph, document and key-value data.
- Scalability and distributed architecture
- Cost effective
- Effective for IOT, content management system and **analytics**.

### Advantages of Neo4j:
- Ideal for Graph database with complex relationships.
- Powerful graph algorithms and advanced graph-specific features.
- Supports Recommendation systems, fraud detection or social network analysis (Which are important for a graph database).
- As it focus mainly on graph data, there are limited support for other data like document or key value (May be a disadvantage).

Other popular databases like **MongoDB, PostgreSQL** and **MySQL** are not primarily graph databases.

| **Database**    | **Native Graph Support** | **Graph Extensions or Features**                  | **Best Use Cases**                                   |
|------------------|---------------------------|--------------------------------------------------|-----------------------------------------------------|
| **Neo4j**       | Yes                       | Native Cypher language, optimized for graph queries. | Complex graphs, social networks, recommendation systems. |
| **ArangoDB**    | Yes                       | Multi-model with AQL for graph queries.            | Mixed workloads with graph and document data.       |
| **MongoDB**     | No                        | Application-level traversals with JSON documents.  | Applications with light graph-like data models.     |
| **PostgreSQL**  | Partial                   | Apache AGE (Cypher), JSON/JSONB support.           | Graph queries alongside relational or JSON data.    |
| **MySQL**       | No                        | Application-level logic for graph-like queries.    | Basic relationships in primarily relational data.   |


We need to decide a data base among them to finalize and choose the pack we need to buy database.

# Final Thoughts:

If our primary goal is working with graph data with higher efficiency we can go for **Neo4j** and if we want a database with versatility and cost effective we can go for **Arango DB**

## References:
Graph database: https://youtu.be/9zwZGjzBRXE?si=oOMEazgO7TkLtO-M
Arango DB and Neo4j reference: https://www.reddit.com/r/Database/comments/1fit1ix/good_graph_database_options/?rdt=36353

@aeroramesh @sajimotrax @nallasivamselvaraj @RajavelRajendiran