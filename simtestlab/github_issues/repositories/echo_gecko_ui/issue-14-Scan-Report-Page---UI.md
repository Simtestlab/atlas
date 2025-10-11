# Issue #14: Scan Report Page - UI

**Repository:** echo_gecko_ui  
**Status:** Closed  
**Created:** 2025-09-13  
**Updated:** 2025-09-18  
**Closed:** 2025-09-18  
**Author:** @harish-ramar  
**Assignees:** @divya-rosy  
**Labels:** `UI/UX`  

[View on GitHub](https://github.com/Simtestlab/echo_gecko_ui/issues/14)

## Description

## Task Overview

<img width="1115" height="1092" alt="Image" src="https://github.com/user-attachments/assets/0ef421d9-7df3-4939-b835-e97100957261" />


The Scan Report screen appears immediately after The Scan Report screen appears immediately after the user completes the Acknowledgement screen. It presents two capture options: take a photo with the device camera or pick an image from the device gallery. Use Flutter UI widgets and official plugins for implementation and keep the UI simple and native-looking.

### Implementation:

- Show this page right after Acknowledgement completion (no server/Firebase calls required).
- Provide two primary actions: Camera: open camera capture flow with a flash toggle and high-quality capture settings.
- Gallery: open the device photo picker to select an existing image. Image quality: choose the device’s highest supported capture quality (e.g., ResolutionPreset.max or highest available).
- For image picker, avoid aggressive compression — keep full resolution or minimal compression to preserve OCR accuracy.
- Flash: provide an on-screen flash control when using the camera. Persist the state while the camera preview is active.
- Permissions: implement and request platform permissions before accessing camera or gallery: Android: declare CAMERA and READ_EXTERNAL_STORAGE (or manage scoped storage) in AndroidManifest.xml and request runtime permissions.
- iOS: add NSCameraUsageDescription and NSPhotoLibraryUsageDescription to Info.plist and request permission at runtime. Use a permission helper (permission_handler or platform APIs) to check, request, and handle denied/blocked states; show a helpful message that guides the user to settings if permission is permanently denied.
- Once the image is captured, update the image to the backend for now. Which can be later modified when the parsing logic is implemented these images can be directly utilized from the server.

### UI:

<img width="210" height="463" alt="Image" src="https://github.com/user-attachments/assets/1f52bb89-aa89-466b-a99d-663387873f6a" />
