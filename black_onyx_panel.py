import bpy


class Black_Onyx_Panel(bpy.types.Panel):
    bl_idname = "Black_Onyx_Panel"
    bl_label = "Black Onyx Panel"
    bl_category = "Black Onyx Addon"
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('view3d.cursor_center', text="Some")
        row.operator('sequencer.zoom_clip', text="Zoom Clip")
