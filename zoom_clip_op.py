import bpy


class Zoom_Clip_Operator(bpy.types.Operator):
    bl_idname = "sequencer.zoom_clip"
    bl_label = "Zoom current clip"
    bl_description = "Zooms current clip"

    def execute(self, context):
        current = context.scene.frame_current
        print(current)
        bpy.ops.view2d.zoom_border(57, 100, 1, 100)
        return {'FINISHED'}
