#-------------------------------------------------------------------------------
#                                    THEME DATA
#-------------------------------------------------------------------------------

TEXT_THEME_DATA = \
'''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>author</key>
    <string>David Saxon</string>
    <key>comment</key>
    <string>A low contrast grey colour scheme</string>
    <key>name</key>
    <string>Circadian</string>
    <key>settings</key>
    <array>
        <dict>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>{background}</string>
                <key>caret</key>
                <string>{caret}</string>
                <key>foreground</key>
                <string>{text}</string>
                <key>invisibles</key>
                <string>#FF38FF</string>
                <key>lineHighlight</key>
                <string>{line_highlight}</string>
                <key>selection</key>
                <string>{selection}</string>
                <key>findHighlight</key>
                <string>{find_highlight}</string>
                <key>inactiveSelection</key>
                <string>{inactive_selection}</string>
                <key>gutterForeground</key>
                <string>{line_numbers}</string>
                <key>guide</key>
                <string>{guide}</string>
                <key>activeGuide</key>
                <string>{guide}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Comment</string>
            <key>scope</key>
            <string>comment</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>italic</string>
                <key>foreground</key>
                <string>{comment}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>String</string>
            <key>scope</key>
            <string>string</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>italic</string>
                <key>foreground</key>
                <string>{string_literal}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Constant</string>
            <key>scope</key>
            <string>constant</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>{literal}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Variable</string>
            <key>scope</key>
            <string>variable</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>{variable}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Keyword</string>
            <key>scope</key>
            <string>keyword</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{keyword}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Storage</string>
            <key>scope</key>
            <string>storage</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{modifier}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Entity Name</string>
            <key>scope</key>
            <string>entity.name</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{entity_name}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Tag Attribute</string>
            <key>scope</key>
            <string>entity.other.attribute-name</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>italic</string>
                <key>foreground</key>
                <string>{text}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library Function</string>
            <key>scope</key>
            <string>support.function</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>{builtin_func}</string>
                <key>fontStyle</key>
                <string>italic</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Objective-C Method Call</string>
            <key>scope</key>
            <string>support.function.any-method</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string></string>
                <key>foreground</key>
                <string>{builtin_func}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library Constant</string>
            <key>scope</key>
            <string>support.constant</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{text}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library Class/Type</string>
            <key>scope</key>
            <string>support.type, support.class</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{modifier}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Library Variable</string>
            <key>scope</key>
            <string>support.variable</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>{text}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Invalid</string>
            <key>scope</key>
            <string>invalid</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>{invalid_background}</string>
                <key>foreground</key>
                <string>{invalid_text}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Include &lt;system&gt;</string>
            <key>scope</key>
            <string>string.quoted.other.lt-gt.include</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>{include_background}</string>
                <key>foreground</key>
                <string>{include_text}</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Include "user"</string>
            <key>scope</key>
            <string>string.quoted.double.include</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>{include_background}</string>
                <key>foreground</key>
                <string>{include_text}</string>
                <key>fontStyle</key>
                <string>italic</string>
            </dict>
        </dict>
    </array>
    <key>uuid</key>
    <string>B0A18BAA-6220-481C-9914-F6D3E51B5410</string>
</dict>
</plist>

'''


UI_THEME_DATA = \
'''
[
//
// TABS
//
    // Tab set
    {{
        "class": "tabset_control",
        "layer0.texture": "Theme - Circadian/Circadian/tabset-background.png",
        "layer0.inner_margin": [10, 0],
        "layer0.opacity":1.0,
        "layer0.tint": {tab_background},
        "content_margin": [0, 4, 0, 0],
        "tab_overlap": 6,
        "tab_width": 160,
        "tab_min_width": 48,
        "tab_height": 34,
        "mouse_wheel_switch": false
    }},
    {{
        "class": "tabset_control",
        "settings": ["mouse_wheel_switches_tabs"],
        "mouse_wheel_switch": true
    }},
    // Tab element
    {{
        "class": "tab_control",
        "content_margin": [14, 0, 14, 6],
        "max_margin_trim": 0,
        "hit_test_level": 0.5,
        // Inactive tab settings
        "layer0.texture": "Theme - Circadian/Circadian/tab.png",
        "layer0.inner_margin": [20, 4],
        "layer0.opacity": 1.0,
        "layer0.tint": {tab_inactive},
        // Active tab setting
        "layer1.texture": "Theme - Circadian/Circadian/tab.png",
        "layer1.inner_margin": [20, 4],
        "layer1.opacity": 0.0,
        "layer1.tint": {tab_active},
        // Hover tab setting
        "layer2.texture": "Theme - Circadian/Circadian/tab.png",
        "layer2.inner_margin": [20, 4],
        "layer2.opacity": 0.0,
        "layer2.tint": {tab_hover}
    }},
    {{
        // Tab close state
        "class": "tab_control",
        "settings": ["show_tab_close_buttons"],
        "content_margin": [12, -5, 8, 4]
    }},
    {{
        // Hover tab state
        "class": "tab_control",
        "attributes": ["hover"],
        "layer2.opacity": 1.0
    }},
    {{
        // Active tab state
        "class": "tab_control",
        "attributes": ["selected"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 1.0,
        "layer2.opacity": 0.0
    }},
    // Tab labels
    {{
        "class": "tab_label",
        "fade": false,
        "fg": {tab_inactive_text},
        "font.bold" : false,
        "font.size" : 11
    }},
    {{
        "class": "tab_label",
        "parents": [{{"class": "tab_control", "attributes": ["hover"]}}],
        "fg": {tab_hover_text}
    }},
    {{
        "class": "tab_label",
        "parents": [{{"class": "tab_control", "attributes": ["selected"]}}],
        "fg": {tab_active_text},  // active tab text
        "shadow_color": [75, 59, 83],
        "shadow_offset": [0, 0]

}},
    // Tab close button
    {{
        "class": "tab_close_button",
        "content_margin": [0, 0],
        // Tab close default settings
        "layer0.texture": "Theme - Flatland/Flatland Dark/tab-close.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 0],
        // Tab close hover settings
        "layer1.texture": "Theme - Flatland/Flatland Dark/tab-close-hover.png",
        "layer1.opacity": 0.0
    }},
    {{
        // Tab button size
        "class": "tab_close_button",
        "settings": ["show_tab_close_buttons"],
        "content_margin": [8, 8]
    }},
    {{
        // Tab close button hover
        "class": "tab_close_button",
        "attributes": ["hover"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 1.0
    }},
    // Tab dirty button
    {{
        "class": "tab_close_button",
        "parents": [{{"class": "tab_control", "attributes": ["dirty"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/tab-dirty.png",
        "layer0.opacity": 1.0,
        "layer1.opacity": 0.0
    }},
    {{
        // Tab dirty button hover
        "class": "tab_close_button",
        "parents": [{{"class": "tab_control", "attributes": ["dirty"]}}],
        "attributes": ["hover"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 1.0
    }},
    {{
        // Tab dirty button active
        "class": "tab_close_button",
        "parents": [{{"class": "tab_control", "attributes": ["selected"]}}],
        "attributes": ["selected"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 0.0
    }},
    // Tab close button hidden with highlight modified flag true
    {{
        // Tab dirty state (close button hidden)
        "class": "tab_control",
        "settings": ["!show_tab_close_buttons", "highlight_modified_tabs"],
        "attributes": ["dirty"],
        "content_margin": [14, 0, 15, 6]
    }},
    {{
        // Tab dirty button (close button hidden)
        "class": "tab_close_button",
        "settings": ["!show_tab_close_buttons", "highlight_modified_tabs"],
        "parents": [{{"class": "tab_control", "attributes": ["dirty"]}}],
        "content_margin": [8, 8],
        "layer0.opacity": 1.0,
        "layer1.opacity": 0.0
    }},
    // SQUARE TABS
    {{
        "class": "tabset_control",
        "settings": ["flatland_square_tabs"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/square/tabset-background.png",
        "content_margin": [0, 0, 0, 0]
        // "tab_overlap": 5
    }},
    {{
        "class": "tab_control",
        "settings": ["flatland_square_tabs"],
        // Inactive tab settings
        "layer0.texture": "Theme - Flatland/Flatland Dark/square/tab-inactive.png",
        // Active tab setting
        "layer1.texture": "Theme - Flatland/Flatland Dark/square/tab-active.png",
        // Hover tab setting
        "layer2.texture": "Theme - Flatland/Flatland Dark/square/tab-hover.png"
    }},

//
// FOLD BUTTONS
//

    {{
        "class": "fold_button_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/fold-closed.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": 0,
        "layer1.texture": "Theme - Flatland/Flatland Dark/fold-closed-pressed.png",
        "layer1.opacity": 0.0,
        "layer1.inner_margin": 0,
        "content_margin": [9, 7, 8, 6]
    }},
    {{
        "class": "fold_button_control",
        "attributes": ["hover"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 0.75
    }},
    {{
        "class": "fold_button_control",
        "attributes": ["pressed"],
        "layer0.opacity": 0.0,
        "layer1.opacity": 1.0
    }},
    {{
        "class": "fold_button_control",
        "attributes": ["expanded"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/fold-open.png",
        "layer1.texture": "Theme - Flatland/Flatland Dark/fold-open-pressed.png"
    }},

//
// STANDARD SCROLLBARS
//

    // Standard vertical scroll bar
    {{
        "class": "scroll_bar_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/standard-scrollbar-vertical.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 6],
        "blur": false
    }},
    // Standard horizontal scroll bar
    {{
        "class": "scroll_bar_control",
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/standard-scrollbar-horizontal.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [6, 0],
        "blur": false
    }},
    // Standard scroll bar corner
    {{
        "class": "scroll_corner_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/standard-scrollbar-corner.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [1, 1]
    }},
    // Standard vertical scroll puck
    {{
        "class": "puck_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/standard-puck-vertical.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 10],
        "content_margin": [8, 12],
        "blur": false
    }},
    // Standard horizontal scroll puck
    {{
        "class": "puck_control",
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/standard-puck-horizontal.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [10, 0],
        "content_margin": [12, 8],
        "blur": false
    }},

//
// OVERLAY SCROLLBARS
//

    // Overlay toggle scroll bar
    {{
        "class": "scroll_area_control",
        "settings": ["overlay_scroll_bars"],
        "overlay": true
    }},
    {{
        "class": "scroll_area_control",
        "settings": ["!overlay_scroll_bars"],
        "overlay": false
    }},
    // Overlay vertical scroll bar
    {{
        "class": "scroll_bar_control",
        "settings": ["overlay_scroll_bars"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-scrollbar-vertical.png",
        "layer0.inner_margin": [0, 5],
        "blur": true
    }},
    // Overlay horizontal scroll bar
    {{
        "class": "scroll_bar_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-scrollbar-horizontal.png",
        "layer0.inner_margin": [5, 0],
        "blur": true
    }},
    // Overlay vertical puck
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-puck-vertical.png",
        "layer0.inner_margin": [0, 5],
        "content_margin": [5, 20],
        "blur": true
    }},
    // Overlay horizontal puck
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-puck-horizontal.png",
        "layer0.inner_margin": [5, 0],
        "content_margin": [20, 5],
        "blur": true
    }},
    // Overlay light puck (for dark content)
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["dark"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-dark-puck-vertical.png"
    }},
    // Overlay light horizontal puck (for dark content)
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal", "dark"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-dark-puck-horizontal.png"
    }},

//
// EMPTY WINDOW BACKGROUND
//

    {{
        "class": "sheet_container_control",
        "layer0.tint": [38,41,44],
        "layer0.opacity": 1.0
    }},

//
// GRID LAYOUT
//
    {{
        "class": "grid_layout_control",
        "border_size": 1,
        "border_color": [70, 70, 70]
    }},

//
// MINI MAP
//

    {{
        "class": "minimap_control",
        "viewport_color": [61, 142, 243, 20]
    }},

//
// LABELS
//

    // General labels
    {{
        "class": "label_control",
        "color": [201, 202, 203],
        "shadow_color": [201, 202, 203],
        "shadow_offset": [0, 0],
        "font.bold" : true,
        "font.size" : 11
    }},
    // Text field labels
    {{
        "class": "label_control",
        "parents": [{{"class": "panel_control"}}],
        "shadow_color": [201, 202, 203],
        "shadow_offset": [0, 0]
    }},
    // Button labels
    {{
        "class": "label_control",
        "parents": [{{"class": "button_control"}}],
        "shadow_color": [201, 202, 203],
        "shadow_offset": [0, 0]
    }},
    // Status bar label
    {{
        "class": "label_control",
        "parents": [{{"class": "status_bar"}}],
        "color": [148, 149, 151],
        "shadow_color": [200, 200, 200],
        "shadow_offset": [0, 0],
        "font.bold" : false
    }},

//
// TOOLTIP
//
    // TODO
    // Tooltip container
    {{
        "class": "tool_tip_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/tooltip.png",
        "layer0.inner_margin": [1, 1],
        "layer0.opacity": 0.95,
        "content_margin": [3, 3]
    }},
    // Tooltip content
    {{
        "class": "tool_tip_label_control",
        "color": [0, 0, 0]
    }},

//
// STATUS BAR
//
    // Status bar container
    {{
        "class": "status_bar",
        "layer0.texture": "Theme - Flatland/Flatland Dark/status-bar-background.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [2, 2],
        "content_margin": [14, 4, 4, 4]
    }},
    {{
        "class": "status_button",
        "min_size": [100, 0]
    }},

//
// SIDEBAR
//

    // Sidebar container
    {{
        "class": "sidebar_container",
        "layer0.tint": [49, 52 ,55],
        "layer0.opacity": 1.0,
        "layer0.draw_center": false,
        "layer0.inner_margin": [0, 0, 0, 0],
        "content_margin": [0, 0, 0, 0]
    }},
    // Sidebar tree
    {{
        "class": "sidebar_tree",
        "row_padding": [8, 4],
        "indent": 14,
        "indent_offset": 20,
        "indent_top_level": false,
        "layer0.tint": {sidebar},
        "layer0.opacity": 1.0,
        "dark_content": false
    }},
    {{
        "class": "sidebar_tree",
        "settings": ["flatland_sidebar_tree_xsmall"],
        "row_padding": [8, 0]
    }},
    {{
        "class": "sidebar_tree",
        "settings": ["flatland_sidebar_tree_small"],
        "row_padding": [8, 2]
    }},
    {{
        "class": "sidebar_tree",
        "settings": ["flatland_sidebar_tree_medium"],
        "row_padding": [8, 3]
    }},
    {{
        "class": "sidebar_tree",
        "settings": ["flatland_sidebar_tree_large"],
        "row_padding": [8, 6]
    }},
    {{
        "class": "sidebar_tree",
        "settings": ["flatland_sidebar_tree_xlarge"],
        "row_padding": [8, 8]
    }},
    // Sidebar rows
    {{
        "class": "tree_row",
        "layer0.texture": "Theme - Flatland/Flatland Dark/sidebar-row-selected.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [1,1]
    }},
    // Settings for gray selected sidebar
    {{
        "settings": ["flatland_gray_selected_sidebar"],
        "class": "tree_row",
        "layer0.texture": "Theme - Flatland/Flatland Dark/sidebar-row-selected-gray.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [1,1]
    }},
    // Sidebar row selected
    {{
        "class": "tree_row",
        "attributes": ["selected"],
        "layer0.opacity": 1.0
    }},
    // Sidebar heading
    {{
        "class": "sidebar_heading",
        "color": [148, 149, 151],
        "font.bold": true,
        "shadow_color": [148, 149, 151],
        "shadow_offset": [0, 0]
    }},
    // Sidebar entry
    {{
        "class": "sidebar_label",
        "color": {sb_file_text},
        "shadow_offset": [0, 0]
    }},
    // Sidebar folder entry
    {{
        "class": "sidebar_label",
        "parents": [{{"class": "tree_row", "attributes": ["expandable"]}}],
        "color": {sb_folder_text},
        "shadow_color": [0, 0, 0],
        "shadow_offset": [0, 0]
    }},
    {{
        "class": "sidebar_label",
        "parents": [{{"class": "tree_row", "attributes": ["expandable", "hover"]}}],
        "color": [255, 255, 255]
    }},
    {{
        "class": "sidebar_label",
        "parents": [{{"class": "tree_row", "attributes": ["expandable"]}}],
        "settings": ["bold_folder_labels"],
        "font.bold": true
    }},
    // Sidebar entry selected
    {{
        "class": "sidebar_label",
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "color": [255, 255, 255],
        "shadow_color": [0, 0, 0],
        "shadow_offset": [0, 0]
    }},
    // Sidebar file close
    {{
        "class": "close_button",
        "layer0.texture": "Theme - Flatland/Flatland Dark/file-close.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": 0,
        "layer1.texture": "Theme - Flatland/Flatland Dark/file-close-selected.png",
        "layer1.opacity": 0.0,
        "layer1.inner_margin": 0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "close_button",
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.opacity": 1.0,
        "layer1.opacity": 0.0
    }},
    {{
        "class": "close_button",
        "parents": [{{"class": "tree_row", "attributes": ["hover", "selected"]}}],
        "layer0.opacity": 0.0,
        "layer1.opacity": 1.0
    }},
    // Sidebar file dirty
    {{
        "class": "close_button",
        "attributes": ["dirty"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/file-dirty.png",
        "layer0.opacity": 1.0
    }},
    {{
        "class": "close_button",
        "attributes": ["dirty"],
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/file-dirty-selected.png"
    }},
    {{
        "class": "close_button",
        "attributes": ["dirty"],
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/file-close.png"
    }},
    // Sidebar file close hover
    {{
        "class": "close_button",
        "attributes": ["hover"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/file-close-hover.png"
    }},
    // Sidebar group closed
    {{
        "class": "disclosure_button_control",
        "content_margin": [0, 6, 18, 7],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-closed.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": 0
    }},
    {{
        "class": "disclosure_button_control",
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-closed.png"
    }},
    {{
        "class": "disclosure_button_control",
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-closed-selected.png"
    }},
    // Sidebar group open
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-open.png"
    }},
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-open.png"
    }},
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/group-open-selected.png"
    }},

//
// HIDE ST3 FILE ICONS FOR NOW (TODO: REMOVE ST2 STYLE ICONS)
//
    {{
        "class": "icon_file_type",
        "content_margin": [0,0]
    }},
    {{
        "class": "icon_folder",
        "content_margin": [0,0]
    }},
    {{
        "class": "icon_folder_loading",
        "layer0.texture":
        {{
            "keyframes":
            [
                "Theme - Flatland/Flatland Dark/spinner/spin_1.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_2.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_3.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_4.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_5.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_6.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_7.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_8.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_9.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_10.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_11.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_12.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_13.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_14.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_15.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_16.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_17.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_18.png",
                "Theme - Flatland/Flatland Dark/spinner/spin_19.png"
            ],
            "loop": true,
            "frame_time": 0.05
        }},
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},


//
// STANDARD TEXT BUTTONS
//

    // Standard buttons (used for Find / Replace panel)
    {{
        "class": "button_control",
        "content_margin": [4, 6, 4, 5],
        "min_size": [69, 0],
        // Default button state
        "layer0.texture": "Theme - Flatland/Flatland Dark/btn-large.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [6, 6],
        // Pressed button setup
        "layer1.texture": "Theme - Flatland/Flatland Dark/btn-large-on.png",
        "layer1.opacity": 0.0,
        "layer1.inner_margin": [6, 6]
    }},
    {{
        // Pressed button state
        "class": "button_control",
        "attributes": ["pressed", "hover"],
        "layer1.opacity": 1.0
    }},

//
// TEXT INPUT FIELD
//

    // Text input field item
    {{
        "class": "text_line_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/text-field.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [10,10,10,10],
        "content_margin": [4, 5, 15, 4]
    }},

//
// PANEL BACKGROUNDS
//

    // Bottom panel background
    {{
        "class": "panel_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/panel-background.png",
        "layer0.inner_margin": [2, 2, 2, 5],
        "layer0.opacity": 1.0
    }},
    // Quick panel background
    {{
        "class": "overlay_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/overlay-bg.png",
        "layer0.inner_margin": [30, 30, 30, 30], // 9grid for the background
        "layer0.opacity": 1.0,
        "layer1.texture": "Theme - Flatland/Flatland Dark/quick-panel-background.png",
        "layer1.inner_margin": [20, 40, 20, 20],
        "layer1.opacity": 1.0,
        "content_margin": [20, 0, 20, 26] // content margin
    }},
    // Square tabs modify height, move content margin for quick panel
    {{
        "class": "overlay_control",
        "settings": ["flatland_square_tabs"],
        "content_margin": [20, 4, 20, 26]
    }},

//
// QUICK PANEL
//

    {{
        "class": "quick_panel",
        "row_padding": [5, 2],
        "layer0.tint": [49, 52, 55],
        "layer0.opacity": 1.0
    }},
    {{
        "class": "quick_panel_row",
        "layer0.texture": "Theme - Flatland/Flatland Dark/quick-panel-row.png",
        "layer0.inner_margin": [2, 2, 2, 2],
        "layer0.opacity": 1.0
    }},
    {{
        "class": "quick_panel_row",
        "attributes": ["selected"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/quick-panel-row-selected.png"
    }},
    {{
        "class": "quick_panel_label",
        "fg": [144, 146, 147],
        "match_fg": [36, 150, 233, 255],
        "selected_fg": [255, 255, 255, 255], //selected foreground
        "selected_match_fg": [37, 40, 43, 255]
    }},
    {{
        "class": "quick_panel_path_label",
        "fg": [104, 106, 107, 255],
        "match_fg": [16, 130, 213, 255],
        "selected_fg": [215, 215, 215, 255],
        "selected_match_fg": [57, 60, 63, 255]
    }},
    {{
        "class": "quick_panel_score_label",
        "fg": [43, 151, 237, 255],
        "selected_fg": [43, 151, 237, 255]
    }},

//
// MINI QUICK PANEL
//

    {{
        "class": "mini_quick_panel_row",
        "layer0.texture": "Theme - Flatland/Flatland Dark/quick-panel-row.png",
        "layer0.inner_margin": [2, 2, 2, 2],
        "layer0.opacity": 1.0
    }},
    {{
        "class": "mini_quick_panel_row",
        "attributes": ["selected"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/quick-panel-row-selected.png"
    }},

//
// CODE COMPLETION DROPDOWN
//
    {{
        "class": "popup_control",
        "content_margin": [0, 0]
    }},
    {{
        "class": "auto_complete",
        "row_padding": [2, 2],
        "layer0.tint": [30, 30, 30],
        "layer0.opacity": 1.0,
        "dark_content": true
    }},
    {{
        "class": "auto_complete_label",
        "fg": [140, 140, 140],
        "match_fg": [255, 255, 255],
        "bg": [26, 26, 26],
        "selected_fg": [255, 255, 255],
        "selected_match_fg": [255, 255, 255],
        "selected_bg": [86, 86, 86]
    }},
    {{
        "class": "table_row",
        "layer0.texture": "Theme - Flatland/Flatland Dark/code-completion-row-selected.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [1, 1]
    }},
    {{
        "class": "table_row",
        "attributes": ["selected"],
        "layer0.opacity": 1.0
    }},

//
// BOTTOM PANEL BUTTONS
//

    // Button group middle
    {{
        "class": "icon_button_control",
        "layer0.texture": "Theme - Flatland/Flatland Dark/btn-group-middle.png",
        "layer0.opacity": 1.0,
        "content_margin": [4, 4,4,5]
    }},
    // Button group left
    {{
        "class": "icon_button_control",
        "attributes": ["left"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/btn-group-left.png",
        "layer0.opacity": 1.0,
        "content_margin": [8,4,5,5]
    }},
    // Button group right
    {{
        "class": "icon_button_control",
        "attributes": ["right"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/btn-group-right.png",
        "layer0.opacity": 1.0,
        "content_margin": [4,4,8,5]
    }},
    // Button single
    {{
        "class": "icon_button_control",
        "attributes": ["left", "right"],
        "layer0.texture": "Theme - Flatland/Flatland Dark/btn-single.png",
        "layer0.opacity": 1.0,
        "content_margin": [8,4,8,5]
    }},

//
// BOTTOM PANEL ICONS - GROUP 1
//

    // Regex search button
    {{
        "class": "icon_regex",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-regex-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_regex",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-regex-on.png"
    }},
    // Case sensitive search button
    {{
        "class": "icon_case",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-case-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_case",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-case-on.png"
    }},
    // Match whole word search button
    {{
        "class": "icon_whole_word",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-word-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_whole_word",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-word-on.png"
    }},

//
// BOTTOM PANEL ICONS - GROUP 1 (EXTENDED: FIND IN FILES)
//

    // Show search context button
    {{
        "class": "icon_context",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-context-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_context",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-context-on.png"
    }},
    // Use search buffer
    {{
        "class": "icon_use_buffer",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-buffer-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_use_buffer",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-buffer-on.png"
    }},

//
// BOTTOM PANEL ICONS - GROUP 2
//

    // Reverse search direction button
    {{
        "class": "icon_reverse",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-reverse-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_reverse",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-reverse-on.png"
    }},
    // Search wrap button
    {{
        "class": "icon_wrap",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-wrap-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_wrap",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-wrap-on.png"
    }},
    // Search in selection button
    {{
        "class": "icon_in_selection",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-selection-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_in_selection",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-selection-on.png"
    }},

//
// BOTTOM PANEL ICONS - GROUP 3
//

    // Preserve case button
    {{
        "class": "icon_preserve_case",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-preserve-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_preserve_case",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-preserve-on.png"
    }},

//
// BOTTOM PANEL ICONS - GROUP 4
//

    // Highlight results button
    {{
        "class": "icon_highlight",
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-highlight-off.png",
        "layer0.opacity": 1.0,
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_highlight",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Flatland/Flatland Dark/icon-highlight-on.png"
    }}

]
'''

#-------------------------------------------------------------------------------
#                                      COLOUR
#-------------------------------------------------------------------------------

class Colour(object):

    def __init__(self, r, g, b, a=-1.0):
        self.__r = r
        self.__g = g
        self.__b = b
        self.__a = a

    def to_hex(self):
        s = '#'
        s += '{0:0{1}x}'.format(int(self.__r * 255.0), 2)
        s += '{0:0{1}x}'.format(int(self.__g * 255.0), 2)
        s += '{0:0{1}x}'.format(int(self.__b * 255.0), 2)
        if(self.__a >= 0.0):
            s += '{0:0{1}x}'.format(int(self.__a * 255.0), 2)
        return s

    def to_tuple(self):
        s = '[{0}, {1}, {2}'.format(
            int(self.__r * 255.0),
            int(self.__g * 255.0),
            int(self.__b * 255.0)
        )
        if(self.__a >= 0.0):
            s += ', {0}'.format(int(self.__a * 255.0))
        s += ']'
        return s


#-------------------------------------------------------------------------------
#                                 DEFAULT COLOURS
#-------------------------------------------------------------------------------

background         = Colour(0.78, 0.95, 1.0)
caret              = Colour(1.0, 0.3, 0.0)
text               = Colour(0.0, 0.0, 0.0)
line_highlight     = Colour(1.0, 1.0, 0.7)
selection          = Colour(1.0, 1.0, 0.0)
inactive_selection = Colour(1.0, 1.0, 0.0, 0.2)
find_highlight     = Colour(1.0, 0.5, 0.0)
line_numbers       = Colour(0.4, 0.4, 0.4)
guide              = Colour(0.4, 0.4, 0.4)
comment            = Colour(0.5, 0.5, 0.5)
literal            = Colour(1.0, 0.05, 0.05)
string_literal     = Colour(0.0, 0.35, 0.0)
keyword            = Colour(0.5, 0.0, 0.5)
entity_name        = Colour(0.3, 0.0, 1.0)
modifier           = Colour(0.8, 0.5, 0.0)
variable           = Colour(0.0, 0.3, 0.2)
builtin_func       = Colour(0.5, 0.0, 0.5)
invalid_background = Colour(1.0, 0.0, 0.0)
invalid_text       = Colour(0.0, 0.0, 0.0)
include_background = Colour(0.4, 0.4, 0.4, 0.4)
include_text       = Colour(0.0, 0.1, 1.0)


sidebar            = Colour(1.0, 1.0, 1.0)
sb_file_text       = Colour(0.2, 0.2, 0.2)
sb_folder_text     = Colour(0.0, 0.0, 0.0)
tab_background     = Colour(1.0, 1.0, 1.0)
tab_active         = Colour(0.85, 0.95, 1.0)
tab_inactive       = Colour(1.0, 1.0, 1.0)
tab_hover          = Colour(0.9, 0.95, 1.0)
tab_active_text    = Colour(0.0, 0.0, 0.0)
tab_inactive_text  = Colour(0.25, 0.25, 0.25)
tab_hover_text     = Colour(0.0, 0.0, 0.0)



#-------------------------------------------------------------------------------
#                                      SCRIPT
#-------------------------------------------------------------------------------

# generate the colours based on the time of day
# TODO

import os

# the file path to where the circadian theme files live
THEME_DIRECTORY = os.path.expanduser(
    '~/.config/sublime-text-2/Packages/Theme - Circadian'
)
# the file path where the text theme file lives
TEXT_THEME_PATH = os.path.join(THEME_DIRECTORY, 'Circadian.tmTheme')
# the file path where the UI theme file lives
UI_THEME_PATH = os.path.join(THEME_DIRECTORY, 'Circadian.sublime-theme')

# write the text theme
with open(TEXT_THEME_PATH, 'w') as f:
    f.write(TEXT_THEME_DATA.format(
        background=background.to_hex(),
        caret=caret.to_hex(),
        text=text.to_hex(),
        line_highlight=line_highlight.to_hex(),
        selection=selection.to_hex(),
        find_highlight=find_highlight.to_hex(),
        inactive_selection=inactive_selection.to_hex(),
        line_numbers=line_numbers.to_hex(),
        guide=guide.to_hex(),
        comment=comment.to_hex(),
        literal=literal.to_hex(),
        string_literal=string_literal.to_hex(),
        keyword=keyword.to_hex(),
        entity_name=entity_name.to_hex(),
        modifier=modifier.to_hex(),
        variable=variable.to_hex(),
        builtin_func=builtin_func.to_hex(),
        invalid_background=invalid_background.to_hex(),
        invalid_text=invalid_text.to_hex(),
        include_background=include_background.to_hex(),
        include_text=include_text.to_hex()
    ))

# write the ui theme
with open(UI_THEME_PATH, 'w') as f:
    f.write(UI_THEME_DATA.format(
        sidebar=sidebar.to_tuple(),
        sb_file_text=sb_file_text.to_tuple(),
        sb_folder_text=sb_folder_text.to_tuple(),
        tab_background=tab_background.to_tuple(),
        tab_active=tab_active.to_tuple(),
        tab_inactive=tab_inactive.to_tuple(),
        tab_hover=tab_hover.to_tuple(),
        tab_active_text=tab_active_text.to_tuple(),
        tab_inactive_text=tab_inactive_text.to_tuple(),
        tab_hover_text=tab_hover_text.to_tuple()
    ))
