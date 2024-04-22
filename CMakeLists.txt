cmake_minimum_required(VERSION 2.8.9)

project(VolumeClip)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/VolumeClip")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Andras Lasso, Matt Lougheed (PerkLab, Queen's University)")
set(EXTENSION_DESCRIPTION "Clip volumes with surface models and ROI boxes")
set(EXTENSION_ICONURL "https://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png")
set(EXTENSION_SCREENSHOTURLS "https://www.slicer.org/slicerWiki/images/4/4c/VolumeClipScreenshot1.png https://www.slicer.org/slicerWiki/images/5/57/VolumeClipScreenshot2.png https://www.slicer.org/slicerWiki/images/1/1a/VolumeClipScreenshot3.png")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(VolumeClipWithModel)
add_subdirectory(VolumeClipWithRoi)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
