import os
import vtk, qt, ctk, slicer
from AbstractScriptedSubjectHierarchyPlugin import *

class VolumeClipSubjectHierarchyPlugin(AbstractScriptedSubjectHierarchyPlugin):
  """ Scripted subject hierarchy plugin for VolumeClipWithRoi and VolumeClipWithModel
      modules.
      
      This is mainly an example for scripted plugins, and has no practical purpose.
  """
  
  # Necessary static member to be able to set python source to scripted subject hierarchy plugin
  filePath = __file__

  def __init__(self, scriptedPlugin):
    scriptedPlugin.name = 'VolumeClip'
    AbstractScriptedSubjectHierarchyPlugin.__init__(self, scriptedPlugin)

  def canOwnSubjectHierarchyNode(self, node):
    if node.IsA('vtkMRMLScalarVolumeNode') and node.GetAttribute("ClippedVolume") is not None:
      return 1.0
    return 0.0

  def roleForPlugin(self):
    return "Clipped volume"
