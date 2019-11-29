# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from . test_op import Test_OT_Operator
from . test_panel import Test_PT_Panel
from . black_onyx_panel import Black_Onyx_Panel
from . zoom_clip_op import Zoom_Clip_Operator

bl_info = {
    "name": "Black Onyx Video Editing Pack",
    "author": "Adrian Szuszkiewicz",
    "description": "A toolset for editing video tutorials in Blender.",
    "blender": (2, 81, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (Test_OT_Operator,
           Test_PT_Panel,
           Black_Onyx_Panel,
           Zoom_Clip_Operator)

register, unregister = bpy.utils.register_classes_factory(classes)
