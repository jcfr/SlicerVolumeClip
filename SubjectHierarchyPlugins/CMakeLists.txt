set(VolumeClipSubjectHierarchyPlugins_PYTHON_SCRIPTS
  __init__
  VolumeClipSubjectHierarchyPlugin
  )

set(VolumeClipSubjectHierarchyPlugins_PYTHON_RESOURCES
  )

ctkMacroCompilePythonScript(
  TARGET_NAME VolumeClipSubjectHierarchyPlugins
  SCRIPTS "${VolumeClipSubjectHierarchyPlugins_PYTHON_SCRIPTS}"
  RESOURCES "${VolumeClipSubjectHierarchyPlugins_PYTHON_RESOURCES}"
  DESTINATION_DIR ${CMAKE_BINARY_DIR}/${Slicer_QTSCRIPTEDMODULES_LIB_DIR}/SubjectHierarchyPlugins
  INSTALL_DIR ${CMAKE_BINARY_DIR}/${Slicer_INSTALL_QTSCRIPTEDMODULES_LIB_DIR}/SubjectHierarchyPlugins
  NO_INSTALL_SUBDIR
  )
