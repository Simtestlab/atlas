# Issue #20: Create Batch File

**Repository:** esysflow  
**Status:** Closed  
**Created:** 2024-11-28  
**Updated:** 2024-12-03  
**Closed:** 2024-12-03  
**Author:** @harish-ramar  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/20)

## Description

# Need to Create a Batch File to run Esysflow:

### Steps To be Done
1. The batch file need to checkout the branch that contains the stable version of esysflow
2. It should check the following system has *Node and Npm* installed and uses the same version esysflow uses. Using the following command:
```
node -v
npm -v
```
3. It should check is *yarn* installed if not we can install using the following command:
```
npm install -g yarn
```
Here -g mentions that yarn should be installed globally.

4. Once, the following package like **Node, Npm and Yarn** installed. We need to install the packages that is need for the project using the following command.
```
yarn install
```

5. After the required packages are installed. We can run the following command to run the project.
```
yarn run dev
```

# Below is an example how the following runs:

![Image](https://github.com/user-attachments/assets/50187333-5e74-41fd-84fb-d4748b7237cc)
![Image](https://github.com/user-attachments/assets/54166791-b8c2-4299-a9b2-55074d14a80c)
![Image](https://github.com/user-attachments/assets/229738f5-e9c2-440d-a8b1-2124e660937d)

**After the commands have been executed visit should visit local host in port 3000. This is how the following URL looks:**
```
http://localhost:3000/
```

@aeroramesh @sajimotrax @nallasivamselvaraj 
