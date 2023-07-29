bl_info = {
    "name": "Custom Object Loader",
    "author": "Mastermind",
    "version": (0, 1,9),
    "blender": (3, 50, 0),
    "description": "This addon is used to add your own custom objects to the Add>Mesh menu in Blender. To do so, go to the N pannel and navigate to the Loader tab. From there, set your desired amount of objects (Max of eight at the moment) and click on the object you want to set. Once you have set your desired file path (Fbx, Obj, Stl, or Dae) and object name, restart Blender. After you boot blender back up your object should be in the Add>Mesh menu."
}

import bpy

import os
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from bpy_extras.io_utils import ImportHelper



from pathlib import Path



if os.path.exists(str(Path.home()) + "\Documents\ObjectLoader"):
    print("Found object loader files")
else:
    print("Unable to find object loader files")
    print("Creating one at " + str(Path.home()) + " Documents/ObjectLoader")
    os.mkdir(str(Path.home()) + "\Documents\ObjectLoader", 0o666)
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotOne.txt","x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotOneName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotTwo.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotTwoName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotThree.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotThreeName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotFour.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotFourName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotFive.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotFiveName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotSix.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotSixName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotSev.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotSevName.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotEight.txt", "x")
    f = open(str(Path.home()) + "\Documents\ObjectLoader\SlotEightName.txt", "x")
    f.close()
    print("Done!")
    b = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "x")
    numberofslots = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "w")
    numberofslots.write("0")
    numberofslots.close()
texts = ""
class OBJECT_PT_TextTool(bpy.types.Panel):
    bl_label = "PrivativeObjectLoader"
    bl_idname = "OBJECT_PT_texttool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Loader"
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row = layout.row()
        row.label(text= "Custom object loader by therealmastermind on discord")
        row = layout.column()
        file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
        numbr = int(file1.read(100))
        row = layout.row()
        row.operator("wm.slounumb", text="+", )
        row = layout.row()
        row.operator("wm.slounumbdown", text="-", )
        row = layout.row()
        row.label(text="Objects")
        row = layout.row()
        if numbr >= 0:
           row.operator("wm.textopbasic", text= "Object One", )
        row = layout.row()
        if numbr >= 1:
            row.operator("wm.textopbasic2", text="Object Two", )
        row = layout.row()
        if numbr >= 2:
             row.operator("wm.textopbasic3", text="Object Three", )
        row = layout.row()
        if numbr >= 3:
            row.operator("wm.textopbasic4", text="Object Four", )
        row = layout.row()
        if numbr >= 4:
            row.operator("wm.textopbasic5", text="Object Five", )
        row = layout.row()
        if numbr >= 5:
            row.operator("wm.textopbasic6", text="Object Six", )
        row = layout.row()
        if numbr >= 6:
            row.operator("wm.textopbasic7", text="Object Seven", )
        row = layout.row()
        if numbr >= 7:
            row.operator("wm.textopbasic8", text="Object Eight", )
        row = layout.row()
        row.label(text="Restart Blender for changes to take effect")
selected_faces = None
class WM_OT_slot_numb(bpy.types.Operator):
    """Increse Slots"""
    bl_idname = "wm.slounumb"
    bl_label = "+"
    home = str(Path.home())
    def execute(self, context):
        file = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
        numb = int(file.read(100))
        file.close()
        if numb != 7:
            numb += 1
        else:
            print("Max amount of slots reached")
        file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "a")
        file1.truncate(0)
        file1.write(str(numb))
        file1.close()
        return {'FINISHED'}

class WM_OT_slot_numbMinus(bpy.types.Operator):
    """Decrese Slots"""
    bl_idname = "wm.slounumbdown"
    bl_label = "-"
    home = str(Path.home())
    def execute(self, context):
        file = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
        numb = int(file.read(100))
        file.close()
        if numb != 0:
            numb -= 1
        else:
            print("Minimum amount of slots reached")
        file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "a")
        file1.truncate(0)
        file1.write(str(numb))
        file1.close()
        return {'FINISHED'}
 
 
 
class WM_OT_textOpBasic(bpy.types.Operator):
    """Set The objects"""
    bl_idname = "wm.textopbasic"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOne.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOneName.txt", "r")
    text : bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        nameFile = self.text2
        selected_faces =self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOne.txt","a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        home = str(Path.home())
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotOneName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}





class WM_OT_textOpBasic2(bpy.types.Operator):
    """Set The objects2"""
    bl_idname = "wm.textopbasic2"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwo.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwoName.txt", "r")
    text : bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2 : bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwo.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwoName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}





class WM_OT_textOpBasic3(bpy.types.Operator):
    """Set The objects3"""
    bl_idname = "wm.textopbasic3"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThree.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThreeName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThree.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThreeName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}




class WM_OT_textOpBasic4(bpy.types.Operator):
    """Set The objects4"""
    bl_idname = "wm.textopbasic4"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFour.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFourName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFour.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFourName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}



class WM_OT_textOpBasic5(bpy.types.Operator):
    """Set The objects5"""
    bl_idname = "wm.textopbasic5"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFive.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFiveName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFive.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotFiveName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}

class WM_OT_textOpBasic6(bpy.types.Operator):
    """Set The objects6"""
    bl_idname = "wm.textopbasic6"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSix.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSixName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSix.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSixName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}

class WM_OT_textOpBasic7(bpy.types.Operator):
    """Set The objects7"""
    bl_idname = "wm.textopbasic7"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSev.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSevName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSev.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotSevName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}

class WM_OT_textOpBasic8(bpy.types.Operator):
    """Set The objects8"""
    bl_idname = "wm.textopbasic8"
    bl_label = "Paste the file path here"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotEight.txt", "r")
    file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotEightName.txt", "r")
    text: bpy.props.StringProperty(name="Set your filepath", default=file1.read(100))
    text2: bpy.props.StringProperty(name="Set the name", default=file2.read(100))
    file1.close()
    file2.close()
    selected_faces = None
    def __init__(self):
        selected_faces = None
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    def execute(self, context):
        selected_faces = self.text
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents\ObjectLoader\SlotEight.txt", "a")
        file1.truncate(0)
        file1.write(selected_faces)
        file1.close()
        print("" + selected_faces)
        nameFile = self.text2
        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotEightName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        return {'FINISHED'}

class ImportOne(bpy.types.Operator):
    """ImportOne"""
    bl_idname = "add.importone"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOneName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    print(my_path)
    bl_label = my_path
    file1.close()
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOne.txt","r")
        my_path = file1.read(100)
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        print("New= " + my_path)
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX") :
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or  my_path.endswith("DAE"):
                bpy.ops.import_scene.dae(filepath=my_path)
            if my_path.endswith("obj") or  my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)

        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}
    



class ImportTwo(bpy.types.Operator):
    """ImportTwo"""
    bl_idname = "add.importtwo"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwoName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwo.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        print("New= " + my_path)
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath = my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)

        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}


class ImportThree(bpy.types.Operator):
    """ImportThree"""
    bl_idname = "add.importthree"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThreeName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThree.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}


class ImportFour(bpy.types.Operator):
    """ImportFour"""
    bl_idname = "add.importfour"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFourName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFour.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}

class ImportFive(bpy.types.Operator):
    """ImportFive"""
    bl_idname = "add.importfive"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFiveName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFive.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}

class ImportSix(bpy.types.Operator):
    """ImportSix"""
    bl_idname = "add.importsix"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotSixName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotSix.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}

class ImportSev(bpy.types.Operator):
    """ImportSev"""
    bl_idname = "add.importsev"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotSevName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotSev.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}

class ImportEight(bpy.types.Operator):
    """ImportEight"""
    bl_idname = "add.importeight"
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotEightName.txt", "r")
    my_path = file1.read(100)
    if my_path == "":
        my_path = "ADD OBJECT HERE"
    bl_label = my_path
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotEight.txt", "r")
        my_path = file1.read(100)
        if my_path == "":
            my_path = "ADD OBJECT HERE"
        file1.close()
        if my_path.startswith('"'):
            my_path = my_path[1:len(my_path) - 1]
            print("Removing marks")
        if os.path.exists(my_path):
            print("File loaded")
            if my_path.endswith("fbx") or my_path.endswith("FBX"):
                bpy.ops.import_scene.fbx(filepath=my_path)
            if my_path.endswith("dae") or my_path.endswith("DAE"):
                bpy.ops.wm.collada_import(filepath=my_path)
            if my_path.endswith("obj") or my_path.endswith("OBJ"):
                bpy.ops.import_scene.obj(filepath=my_path)
            if my_path.endswith("stl") or  my_path.endswith("STL"):
                bpy.ops.import_mesh.stl(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  


def menu_func(self, context):
    file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
    numbr = int(file1.read(100))
    if numbr >= 0:
         self.layout.operator(ImportOne.bl_idname)
    if numbr >= 1:
        self.layout.operator(ImportTwo.bl_idname)
    if numbr >= 2:
        self.layout.operator(ImportThree.bl_idname)
    if numbr >= 3:
        self.layout.operator(ImportFour.bl_idname)
    if numbr >= 4:
        self.layout.operator(ImportFive.bl_idname)
    if numbr >= 5:
        self.layout.operator(ImportSix.bl_idname)
    if numbr >= 6:
        self.layout.operator(ImportSev.bl_idname)
    if numbr >= 7:
        self.layout.operator(ImportSev.bl_idname)

def register():
    print("registering clases.....")
    bpy.utils.register_class(WM_OT_slot_numb)
    bpy.utils.register_class(WM_OT_slot_numbMinus)
    bpy.utils.register_class(ImportOne)
    bpy.utils.register_class(ImportTwo)
    bpy.utils.register_class(ImportThree)
    bpy.utils.register_class(ImportFour)
    bpy.utils.register_class(ImportFive)
    bpy.utils.register_class(ImportSix)
    bpy.utils.register_class(ImportSev)
    bpy.utils.register_class(ImportEight)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(OBJECT_PT_TextTool)
    bpy.utils.register_class(WM_OT_textOpBasic)
    bpy.utils.register_class(WM_OT_textOpBasic2)
    bpy.utils.register_class(WM_OT_textOpBasic3)
    bpy.utils.register_class(WM_OT_textOpBasic4)
    bpy.utils.register_class(WM_OT_textOpBasic5)
    bpy.utils.register_class(WM_OT_textOpBasic6)
    bpy.utils.register_class(WM_OT_textOpBasic7)
    bpy.utils.register_class(WM_OT_textOpBasic8)
    print("Done!")

def unregister():
    slotnumb2 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
    numbr = int(slotnumb2.read(100))
    bpy.utils.unregister_class(WM_OT_slot_numb)
    bpy.utils.unregister_class(WM_OT_slot_numbMinus)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    bpy.utils.unregister_class(ImportOne)
    bpy.utils.unregister_class(ImportTwo)
    bpy.utils.unregister_class(ImportThree)
    bpy.utils.unregister_class(ImportFour)
    bpy.utils.unregister_class(ImportFive)
    bpy.utils.unregister_class(ImportSix)
    bpy.utils.unregister_class(ImportSev)
    bpy.utils.unregister_class(ImportEight)
    bpy.utils.unregister_class(OBJECT_PT_TextTool)
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic)
    except:
        print("")
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic2)
    except:
        print("")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic3)
    except:
        print("")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic4)
    except:
        print("")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic5)
    except:
        print("")
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic6)
    except:
        print("")
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic7)
    except:
        print("")
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic8)
    except:
        print("")



if __name__ == "__main__":
    register()