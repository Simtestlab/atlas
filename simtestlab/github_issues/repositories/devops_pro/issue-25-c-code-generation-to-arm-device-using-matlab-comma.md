# Issue #25: c code generation to arm device using matlab command

**Repository:** devops_pro  
**Status:** Open  
**Created:** 2024-12-07  
**Updated:** 2024-12-07  
**Author:** @nallasivamselvaraj  
**Assignees:** @nallasivamselvaraj  

[View on GitHub](https://github.com/Simtestlab/devops_pro/issues/25)

## Description

**Issue with Generating C Code for ARM Cortex-M Using MATLAB Commands**

I am trying to generate C code for ARM-compatible hardware (ARM Cortex-M) using MATLAB commands.

**Observations:**

- When generating C code using Simulink, the parameter settings work correctly, and the code generation process is successful.
- However, when using MATLAB commands for code generation, the parameters are not set properly.
- Additionally, if I attempt to create the code using MATLAB scripts initially, it fails due to incorrect parameter settings. 
- if I use -Simulink first and then run the commands, the code is generated successfully.

**Request:**
I need suggestions for correctly setting parameters when generating C code via MATLAB commands.

Following Parameters set by ui 

![Image](https://github.com/user-attachments/assets/53a45064-cdfc-4298-97b5-89b38114fe81)
![Image](https://github.com/user-attachments/assets/093fe28d-65ef-47c3-896d-bc270913e83e)
![Image](https://github.com/user-attachments/assets/e86b78df-0a0d-4e1b-bbd1-8520ea06cea7)


parameter by commands 

### Configure Subsystem for Code Generation

```matlab
% Model and subsystem name
modelName = 'BMSContactorControl'; % Model 
subsystemName = 'BMSContactorControl'; % Subsystem 

% Path to the subsystem
subsystemPath = [modelName, '/', subsystemName];

% Load the model
load_system(modelName);

% Configure Subsystem for Code Generation
set_param(subsystemPath, 'SystemTargetFile', 'ert.tlc'); % Use Embedded Coder
set_param(subsystemPath, 'GenerateCodeOnly', 'on'); % Generate code 
set_param(subsystemPath, 'SingleInstanceERTCode', 'on'); % Enable 

% Target Hardware Settings
set_param(modelName, 'HardwareImplementation', 'on');
set_param(modelName, 'HWDeviceType', 'ARM Compatible->ARM Cortex-M'); % ARM Cortex-M

% Optimization Settings
set_param(subsystemPath, 'ExecutionEfficiency', 'on'); 
set_param(subsystemPath, 'OptimizeModel', 'on');
set_param(subsystemPath, 'InlineInvariantSignals', 'on'); 
set_param(subsystemPath, 'RemoveInternalDataZeroInit', 'on');

% Word Length Settings
set_param(subsystemPath, 'ProdWordSize', '32'); 
set_param(subsystemPath, 'ProdHWDeviceType', 'ARM Compatible->ARM Cortex-M');

% Save and Close the Model
save_system(modelName);
close_system(modelName);

disp('Embedded Code done.');
###

@RajavelRajendiran @aeroramesh 
 

