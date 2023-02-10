bl_info = {
    "name": "Object Loader",
    "author": "Mastermind",
    "version": (0, 5,1),
    "blender": (3, 40, 0),
    "description": "An addon for adding custom objects to Add>Mesh"
}

import bpy

import os
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


from pathlib import Path



if os.path.exists(str(Path.home()) + "\Documents\ObjectLoader"):
    print("Folder Exists")
else:
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
    b = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "x")
    numberofslots = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "w")
    numberofslots.truncate(0)
    numberofslots.write("0")


 
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
        row.label(text= "Number of objects")
        row = layout.column()
        
       # row = layout.split(factor= -0.9)

        file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
        numbr = int(file1.read(100))
        row = layout.row()

        row.operator("wm.slounumb", text="Number of objects", )
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
        row.label(text="Restart Blender for changes to take effect")
 
 
 
 
 

selected_faces = None


class WM_OT_slot_numb(bpy.types.Operator):
    """Set the number"""
    bl_idname = "wm.slounumb"
    bl_label = "number of slots"
    home = str(Path.home())
    file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
    text: bpy.props.StringProperty(name="Number of slots (Must restart blender for changes to take effect", default=file1.read(100))
    file1.close()


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        numb = self.text
        file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "a")
        file1.truncate(0)
        file1.write(numb)
        file1.close()
        return {'FINISHED'}
 
 
 
class WM_OT_textOpBasic(bpy.types.Operator):
    """Set The objects"""
    bl_idname = "wm.textopbasic"
    bl_label = "                            FilePath"
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
        print("" +nameFile)
        
       # t = self.text
        
        #bpy.ops.object.text_add(enter_editmode=True)
 
        return {'FINISHED'}





class WM_OT_textOpBasic2(bpy.types.Operator):
    """Set The objects2"""
    bl_idname = "wm.textopbasic2"
    bl_label = "Paste the fbx file path (No Quotation marks)"
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
        print("" + selected_faces)
        nameFile = self.text2

        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotTwoName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}





class WM_OT_textOpBasic3(bpy.types.Operator):
    """Set The objects3"""
    bl_idname = "wm.textopbasic3"
    bl_label = "Paste the fbx file path (No Quotation marks)"
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
        print("" + selected_faces)
        nameFile = self.text2

        file2 = open(str(Path.home())+"\Documents\ObjectLoader\SlotThreeName.txt", "a")
        file2.truncate(0)
        file2.write(nameFile)
        file2.close()
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}




class WM_OT_textOpBasic4(bpy.types.Operator):
    """Set The objects4"""
    bl_idname = "wm.textopbasic4"
    bl_label = "Paste the fbx file path (No Quotation marks)"
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
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}



class WM_OT_textOpBasic5(bpy.types.Operator):
    """Set The objects5"""
    bl_idname = "wm.textopbasic5"
    bl_label = "Paste the fbx file path (No Quotation marks)"
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
        print("" + nameFile)

        # t = self.text

        # bpy.ops.object.text_add(enter_editmode=True)

        return {'FINISHED'}

class ImportOne(bpy.types.Operator):
    """ImportOne"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importone"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOneName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    file1.close()
    bl_options = {'REGISTER', 'UNDO'}
    
        

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotOne.txt","r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.
    



class ImportTwo(bpy.types.Operator):
    """ImportTwo"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importtwo"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwoName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotTwo.txt", "r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


class ImportThree(bpy.types.Operator):
    """ImportThree"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importthree"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThreeName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotThree.txt", "r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


class ImportFour(bpy.types.Operator):
    """ImportFour"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importfour"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFourName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFour.txt", "r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


class ImportFive(bpy.types.Operator):
    """ImportFive"""  # Use this as a tooltip for menu items and buttons.
    bl_idname = "add.importfive"  # Unique identifier for buttons and menu items to reference.
    home = str(Path.home())
    file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFiveName.txt", "r")
    my_path = file1.read(100)
    bl_label = my_path  # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        home = str(Path.home())
        file1 = open(str(Path.home())+"\Documents/ObjectLoader/SlotFive.txt", "r")
        my_path = file1.read(100)
        print(my_path)
        file1.close()
        if os.path.exists(my_path):
            print("File loaded")
            bpy.ops.import_scene.fbx(filepath=my_path)
        else:
            print("File could not be found")
        for item in bpy.data.materials:
            item.blend_method = 'OPAQUE'
        return {'FINISHED'}  # Lets Blender know the operator finished successfully.


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
 
    
 
 
 
 
 
def register():
    file1 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
    numbr = int(file1.read(100))


    bpy.utils.register_class(WM_OT_slot_numb)


    bpy.utils.register_class(ImportOne)
    bpy.utils.register_class(ImportTwo)
    bpy.utils.register_class(ImportThree)
    bpy.utils.register_class(ImportFour)
    bpy.utils.register_class(ImportFive)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    bpy.utils.register_class(OBJECT_PT_TextTool)

    bpy.utils.register_class(WM_OT_textOpBasic)

    bpy.utils.register_class(WM_OT_textOpBasic2)

    bpy.utils.register_class(WM_OT_textOpBasic3)

    bpy.utils.register_class(WM_OT_textOpBasic4)

    bpy.utils.register_class(WM_OT_textOpBasic5)

    file1.close()

def unregister():
    slotnumb2 = open(str(Path.home()) + "\Documents\ObjectLoader\SlotNumb.txt", "r")
    numbr = int(slotnumb2.read(100))
    bpy.utils.unregister_class(WM_OT_slot_numb)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    bpy.utils.unregister_class(ImportOne)
    bpy.utils.unregister_class(ImportTwo)
    bpy.utils.unregister_class(ImportThree)
    bpy.utils.unregister_class(ImportFour)
    bpy.utils.unregister_class(ImportFive)
    bpy.utils.unregister_class(OBJECT_PT_TextTool)

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic)
    except:
        print("An exception occurred")
    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic2)
    except:
        print("An exception occurred")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic3)
    except:
        print("An exception occurred")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic4)
    except:
        print("An exception occurred")

    try:
        bpy.utils.unregister_class(WM_OT_textOpBasic5)
    except:
        print("An exception occurred")



if __name__ == "__main__":
    register()