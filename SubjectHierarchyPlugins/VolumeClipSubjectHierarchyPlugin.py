import os
import vtk, qt, ctk, slicer
import logging
from AbstractScriptedSubjectHierarchyPlugin import *

class VolumeClipSubjectHierarchyPlugin(AbstractScriptedSubjectHierarchyPlugin):
  """ Scripted subject hierarchy plugin for VolumeClipWithRoi and VolumeClipWithModel
      modules.
      
      This is mainly an example for scripted plugins, and has no practical purpose.
      The methods that are not needed (i.e. the default implementation in
      qSlicerSubjectHierarchyAbstractPlugin is satisfactory) can simply be omitted.
  """
  
  # Necessary static member to be able to set python source to scripted subject hierarchy plugin
  filePath = __file__

  def __init__(self, scriptedPlugin):
    scriptedPlugin.name = 'VolumeClip'
    AbstractScriptedSubjectHierarchyPlugin.__init__(self, scriptedPlugin)

    self.celebrateNodeAction = qt.QAction("Celebrate node (sample action)", scriptedPlugin)
    self.celebrateNodeAction.connect("triggered()", self.onCelebrateNode)

    self.celebrateSceneAction = qt.QAction("Celebrate scene (sample action)", scriptedPlugin)
    self.celebrateSceneAction.connect("triggered()", self.onCelebrateScene)

  def canOwnSubjectHierarchyNode(self, node):
    associatedNode = node.GetAssociatedNode()
    if (associatedNode is not None and
        associatedNode.IsA('vtkMRMLScalarVolumeNode') and
        associatedNode.GetAttribute("ClippedVolume") is not None):
      return 1.0
    return 0.0

  def roleForPlugin(self):
    return "Clipped volume"

  def helpText(self):
    return ("<p style=\" margin-top:4px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
      "<span style=\" font-family:'sans-serif'; font-size:9pt; font-weight:600; color:#000000;\">"
      "VolumeClip module sample subject hierarchy help text"
      "</span>"
      "</p>"
      "<p style=\" margin-top:0px; margin-bottom:11px; margin-left:26px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
      "<span style=\" font-family:'sans-serif'; font-size:9pt; color:#000000;\">"
      "This is how you can add help text to the subject hierarchy module help box via a python scripted plugin."
      "</span>"
      "</p>\n")

  def icon(self, node):
    iconPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons/VolumeClip.png')
    if self.canOwnSubjectHierarchyNode(node) > 0.0 and os.path.exists(iconPath):
      return qt.QIcon(iconPath)
    # Node unknown by plugin
    return qt.QIcon()

  def visibilityIcon(self, visible):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    return pluginHandlerSingleton.pluginByName('Volumes').visibilityIcon(visible)

  def editProperties(self, node):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    pluginHandlerSingleton.pluginByName('Volumes').editProperties(node)

  def nodeContextMenuActions(self):
    return [self.celebrateNodeAction]
  
  def onCelebrateNode(self):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    currentNode = pluginHandlerSingleton.currentNode()
    if currentNode is None:
      logging.error("Invalid current node!")
    message = "Celebrating node " + currentNode.GetName() + "...\n\nHooray!"
    qt.QMessageBox.information(slicer.util.mainWindow(), "Celebrate node (sample action)", message)

  def sceneContextMenuActions(self):
    return [self.celebrateSceneAction]

  def onCelebrateScene(self):
    qt.QMessageBox.information(slicer.util.mainWindow(), "Celebrate scene (sample action)", "Celebrating scene...\n\nHooray!")

  def showContextMenuActionsForNode(self, node):
    # Scene
    if node is None:
      self.celebrateSceneAction.visible = True
    # Node
    if (node is not None and
        self.canOwnSubjectHierarchyNode(node) and
        self.scriptedPlugin.isThisPluginOwnerOfNode(node)):
      self.celebrateNodeAction.visible = True

  def tooltip(self, node):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    tooltip = str(pluginHandlerSingleton.pluginByName('Volumes').tooltip(node))
    associatedNode = node.GetAssociatedNode()
    if associatedNode:
      inputNodeID = associatedNode.GetAttribute("ClippedVolume")
      if inputNodeID is not None:
        inputNode = slicer.util.getNode(inputNodeID)
        tooltip += " (Clipped from node " + inputNode.GetName() + ")"
    return tooltip
        
  def setDisplayVisibility(self, node, visible):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    pluginHandlerSingleton.pluginByName('Volumes').setDisplayVisibility(node, visible)

  def getDisplayVisibility(self, node):
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    return pluginHandlerSingleton.pluginByName('Volumes').getDisplayVisibility(node)
