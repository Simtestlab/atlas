# Issue #359: 1.3 Create an API to store and fetch data from a database.

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-08-09  
**Updated:** 2025-08-09  
**Author:** @divya-rosy  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/359)

## Description

We need a GET, POST, PUT and DELETE APIs for the documentation data with a separate table, it should use **node id** as **Primary key**. The documentation data will be in a JSON format so we need to ensure the database and the APIs should handle it properly. Initially can be tested, its  functionality with postman later can be integrated in the UI.

**JSON Structure:**
	type: 'doc',
content: [
   { type: 'heading', attrs: { level: 1 }, content: [{ type: 'text', text: 'Hello world' }] },
   {
     type: 'paragraph',
     content: [
       { type: 'text', text: 'Hello ' },
       { type: 'text', marks: [{ type: 'italic' }], text: 'word' },
     ],
   }

**Expected table Structure:**
	Note: The database can be structured the way mentioned above or can be modified based on other table’s requirements. We need to define an entire database that supports the features like state management, comment history etc…

