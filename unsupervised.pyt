import arcpy
from arcpy.sa import *
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName = "Input raster layer",
            name = "select_raster",
            datatype = "Raster Layer",
            parameterType = "Required",
            direction = "Input")

        param1 = arcpy.Parameter(
            displayName = "Enter number of classes",
            name = "num_classes",
            datatype = "String",
            parameterType = "Required",
            direction = "Input")

        param2 = arcpy.Parameter(
            displayName = "Enter minimum number of cells to make a valid class",
            name = "num_cells",
            datatype = "String",
            parameterType = "Required",
            direction = "Input")

        param3 = arcpy.Parameter(
            displayName = "Output feature layer",
            name = "output_location",
            datatype = "Feature Layer",
            parameterType = "Required",
            direction = "Output")

        params = [param0,param1,param2,param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # Check out the ArcGIS Spatial Analyst extension licence
        arcpy.CheckExtension('Spatial')

        # set local variables
        param0 = parameters[0].valueAsText  # input raster
        param1 = parameters[1].valueAsText  # number of classes for classification
        param2 = parameters[2].valueASText  # minimum number of cells to make a valid class
        param3 = parameters[3].valueASText  # output layer name and destination
        sampInterval = 15

        # Execute IsoCluster
        outUnsupervised = IsoClusterUnsupervisedClassification(param0, param1,param2,sampInterval)

        arcpy.RasterToPolygon_conversion(outUnsupervised,param3)

        return