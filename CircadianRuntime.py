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
    <string>A dynamic colour scheme to match the time of day</string>
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
        "layer0.texture": "Theme - Circadian/Circadian/tab-close.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 0],
        "layer0.tint": {tab_close},
        // Tab close hover settings
        "layer1.texture": "Theme - Circadian/Circadian/tab-close.png",
        "layer1.opacity": 0.0,
        "layer1.tint": {tab_close_hover}
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
        "layer0.texture": "Theme - Circadian/Circadian/tab-dirty.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {tab_dirty},
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

//
// FOLD BUTTONS
//

    {{
        "class": "fold_button_control",
        "layer0.texture": "Theme - Circadian/Circadian/fold-closed.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": 0,
        "layer0.tint": {fold_closed},
        "layer1.texture": "Theme - Circadian/Circadian/fold-closed.png",
        "layer1.opacity": 0.0,
        "layer1.inner_margin": 0,
        "layer1.tint": {fold_closed_pressed},
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
        "layer0.texture": "Theme - Circadian/Circadian/fold-open.png",
        "layer0.tint": {fold_open},
        "layer1.texture": "Theme - Circadian/Circadian/fold-open.png",
        "layer1.tint": {fold_open_pressed}
    }},

//
// STANDARD SCROLLBARS
//

    // Standard vertical scroll bar
    {{
        "class": "scroll_bar_control",
        "layer0.texture": "Theme - Circadian/Circadian/standard-scrollbar.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 6],
        "layer0.tint": {scroll_bar_background},
        "blur": false
    }},
    // Standard horizontal scroll bar
    {{
        "class": "scroll_bar_control",
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Circadian/Circadian/standard-scrollbar.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [6, 0],
        "layer0.tint": {scroll_bar_background},
        "blur": false
    }},
    // Standard scroll bar corner
    {{
        "class": "scroll_corner_control",
        "layer0.texture": "Theme - Circadian/Circadian/standard-scrollbar.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [1, 1],
        "layer0.tint": {scroll_bar_corner}
    }},
    // Standard vertical scroll puck
    {{
        "class": "puck_control",
        "layer0.texture": "Theme - Circadian/Circadian/standard-puck-vertical.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [0, 10],
        "layer0.tint": {scroll_puck},
        "content_margin": [8, 12],
        "blur": false
    }},
    // Standard horizontal scroll puck
    {{
        "class": "puck_control",
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Circadian/Circadian/standard-puck-horizontal.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [10, 0],
        "layer0.tint": {scroll_puck},
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
        "layer0.texture": "Theme - Circadian/Circadian/overlay-scrollbar-vertical.png",
        "layer0.inner_margin": [0, 5],
        "blur": true
    }},
    // Overlay horizontal scroll bar
    {{
        "class": "scroll_bar_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Circadian/Circadian/overlay-scrollbar-horizontal.png",
        "layer0.inner_margin": [5, 0],
        "blur": true
    }},
    // Overlay vertical puck
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "layer0.texture": "Theme - Circadian/Circadian/overlay-puck-vertical.png",
        "layer0.inner_margin": [0, 5],
        "content_margin": [5, 20],
        "blur": true
    }},
    // Overlay horizontal puck
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal"],
        "layer0.texture": "Theme - Circadian/Circadian/overlay-puck-horizontal.png",
        "layer0.inner_margin": [5, 0],
        "content_margin": [20, 5],
        "blur": true
    }},
    // Overlay light puck (for dark content)
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["dark"],
        "layer0.texture": "Theme - Circadian/Circadian/overlay-dark-puck-vertical.png"
    }},
    // Overlay light horizontal puck (for dark content)
    {{
        "class": "puck_control",
        "settings": ["overlay_scroll_bars"],
        "attributes": ["horizontal", "dark"],
        "layer0.texture": "Theme - Circadian/Circadian/overlay-dark-puck-horizontal.png"
    }},

//
// EMPTY WINDOW BACKGROUND
//

    {{
        "class": "sheet_container_control",
        "layer0.tint": {empty_window},
        "layer0.opacity": 1.0
    }},

//
// GRID LAYOUT
//
    {{
        "class": "grid_layout_control",
        "border_size": 1,
        "border_color": {layout_divider}
    }},

//
// MINI MAP
//

    {{
        "class": "minimap_control",
        "viewport_color": {minimap}
    }},

//
// LABELS
//

    // General labels
    {{
        "class": "label_control",
        "color": {large_button_text},
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
        "color": {status_bar_label},
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
        "layer0.texture": "Theme - Circadian/Circadian/tooltip.png",
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
        "layer0.texture": "Theme - Circadian/Circadian/status-bar-background.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [2, 2],
        "layer0.tint": {status_bar},
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
        "layer0.tint": {sidebar},
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
        "layer0.texture": "Theme - Circadian/Circadian/sidebar-row-selected.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [1,1],
        "layer0.tint": {sidebar_selected}
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
        "color": {sidebar_heading},
        "font.bold": true,
        "shadow_color": [0, 0, 0],
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
        "color": {sb_file_text_hover}
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
        "color": {sb_file_text_selected},
        "shadow_color": [0, 0, 0],
        "shadow_offset": [0, 0]
    }},
    // Sidebar file close
    {{
        "class": "close_button",
        "layer0.texture": "Theme - Circadian/Circadian/file-close.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": 0,
        "layer1.texture": "Theme - Circadian/Circadian/file-close-selected.png",
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
        "layer0.texture": "Theme - Circadian/Circadian/file-dirty.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {tab_dirty}
    }},
    {{
        "class": "close_button",
        "attributes": ["dirty"],
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/file-dirty-selected.png",
        "layer0.tint": {sb_file_text_selected}

    }},
    {{
        "class": "close_button",
        "attributes": ["dirty"],
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/file-close.png"
    }},
    // Sidebar file close hover
    {{
        "class": "close_button",
        "attributes": ["hover"],
        "layer0.texture": "Theme - Circadian/Circadian/file-close-hover.png"
    }},
    // Sidebar group closed
    {{
        "class": "disclosure_button_control",
        "content_margin": [0, 6, 18, 7],
        "layer0.texture": "Theme - Circadian/Circadian/group-closed.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": 0,
        "layer0.tint": {sb_folder_icon}
    }},
    {{
        "class": "disclosure_button_control",
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/group-closed.png",
        "layer0.tint": {sb_folder_icon_hover}
    }},
    {{
        "class": "disclosure_button_control",
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/group-closed.png",
        "layer0.tint": {sb_folder_icon_selected}
    }},
    // Sidebar group open
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "layer0.texture": "Theme - Circadian/Circadian/group-open.png",
        "layer0.tint": {sb_folder_icon}
    }},
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "parents": [{{"class": "tree_row", "attributes": ["hover"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/group-open.png",
        "layer0.tint": {sb_folder_icon_hover}
    }},
    {{
        "class": "disclosure_button_control",
        "attributes": ["expanded"],
        "parents": [{{"class": "tree_row", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/group-open.png",
        "layer0.tint": {sb_folder_icon_selected}
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
                "Theme - Circadian/Circadian/spinner/spin_1.png",
                "Theme - Circadian/Circadian/spinner/spin_2.png",
                "Theme - Circadian/Circadian/spinner/spin_3.png",
                "Theme - Circadian/Circadian/spinner/spin_4.png",
                "Theme - Circadian/Circadian/spinner/spin_5.png",
                "Theme - Circadian/Circadian/spinner/spin_6.png",
                "Theme - Circadian/Circadian/spinner/spin_7.png",
                "Theme - Circadian/Circadian/spinner/spin_8.png",
                "Theme - Circadian/Circadian/spinner/spin_9.png",
                "Theme - Circadian/Circadian/spinner/spin_10.png",
                "Theme - Circadian/Circadian/spinner/spin_11.png",
                "Theme - Circadian/Circadian/spinner/spin_12.png",
                "Theme - Circadian/Circadian/spinner/spin_13.png",
                "Theme - Circadian/Circadian/spinner/spin_14.png",
                "Theme - Circadian/Circadian/spinner/spin_15.png",
                "Theme - Circadian/Circadian/spinner/spin_16.png",
                "Theme - Circadian/Circadian/spinner/spin_17.png",
                "Theme - Circadian/Circadian/spinner/spin_18.png",
                "Theme - Circadian/Circadian/spinner/spin_19.png"
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
        "layer0.texture": "Theme - Circadian/Circadian/btn-large.png",
        "layer0.opacity": 1.0,
        "layer0.inner_margin": [6, 6],
        "layer0.tint": {large_button},
        // Pressed button setup
        "layer1.texture": "Theme - Circadian/Circadian/btn-large.png",
        "layer1.opacity": 0.0,
        "layer1.inner_margin": [6, 6],
        "layer1.tint": {large_button_pressed}
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
        "layer0.texture": "Theme - Circadian/Circadian/text-field.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [10,10,10,10],
        "content_margin": [4, 5, 15, 4]
    }},

//
// PANEL BACKGROUNDS
//

    // Bottom panel background
    {{
        "class": "panel_control",
        "layer0.texture": "Theme - Circadian/Circadian/panel-background.png",
        "layer0.inner_margin": [2, 2, 2, 5],
        "layer0.opacity": 1.0,
        "layer0.tint": {panel_background}
    }},
    // Quick panel background
    {{
        "class": "overlay_control",
        "layer0.texture": "Theme - Circadian/Circadian/overlay-bg.png",
        "layer0.inner_margin": [30, 30, 30, 30], // 9grid for the background
        "layer0.opacity": 1.0,
        "layer0.tint": {quick_panel_background},
        "layer1.texture": "Theme - Circadian/Circadian/quick-panel-background.png",
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
        "layer0.texture": "Theme - Circadian/Circadian/quick-panel-row.png",
        "layer0.inner_margin": [2, 2, 2, 2],
        "layer0.opacity": 1.0,
        "layer0.tint": {qp_row}
    }},
    {{
        "class": "quick_panel_row",
        "attributes": ["selected"],
        "layer0.texture": "Theme - Circadian/Circadian/quick-panel-row.png",
        "layer0.tint": {qp_row_selected}
    }},
    {{
        "class": "quick_panel_label",
        "fg": {qp_text},
        "match_fg": {qp_text_match},
        "selected_fg": {qp_text_selected},
        "selected_match_fg": {qp_text_match_selected}
    }},
    {{
        "class": "quick_panel_path_label",
        "fg": {qp_text},
        "match_fg": {qp_text_match},
        "selected_fg": {qp_text_selected},
        "selected_match_fg": {qp_text_match_selected}
    }},
    {{
        "class": "quick_panel_score_label",
        "fg": {qp_text_score},
        "selected_fg": {qp_text_score_selected}
    }},

//
// MINI QUICK PANEL
//

    {{
        "class": "mini_quick_panel_row",
        "layer0.texture": "Theme - Circadian/Circadian/quick-panel-row.png",
        "layer0.inner_margin": [2, 2, 2, 2],
        "layer0.opacity": 1.0,
        "layer0.tint": {qp_row}
    }},
    {{
        "class": "mini_quick_panel_row",
        "attributes": ["selected"],
        "layer0.texture": "Theme - Circadian/Circadian/quick-panel-row.png",
        "layer0.tint": {qp_row_selected}
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
        "layer0.tint": {ac_background},
        "layer0.opacity": 1.0,
        "dark_content": true
    }},
    {{
        "class": "auto_complete_label",
        "fg": {ac_text},
        "match_fg": {ac_text_match},
        "bg": [26, 26, 26],
        "selected_fg": {ac_text_selected},
        "selected_match_fg": {ac_text_match_selected},
        "selected_bg": [86, 86, 86]
    }},
    {{
        "class": "table_row",
        "layer0.texture": "Theme - Circadian/Circadian/code-completion-row-selected.png",
        "layer0.opacity": 0.0,
        "layer0.inner_margin": [1, 1],
        "layer0.tint": {ac_row_selected}
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
        "layer0.texture": "Theme - Circadian/Circadian/btn-group-middle.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {large_button},
        "content_margin": [4, 4,4,5]
    }},
    // Button group left
    {{
        "class": "icon_button_control",
        "attributes": ["left"],
        "layer0.texture": "Theme - Circadian/Circadian/btn-group-left.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {large_button},
        "content_margin": [8,4,5,5]
    }},
    // Button group right
    {{
        "class": "icon_button_control",
        "attributes": ["right"],
        "layer0.texture": "Theme - Circadian/Circadian/btn-group-right.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {large_button},
        "content_margin": [4,4,8,5]
    }},
    // Button single
    {{
        "class": "icon_button_control",
        "attributes": ["left", "right"],
        "layer0.texture": "Theme - Circadian/Circadian/btn-single.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {large_button},
        "content_margin": [8,4,8,5]
    }},

//
// BOTTOM PANEL ICONS - GROUP 1
//

    // Regex search button
    {{
        "class": "icon_regex",
        "layer0.texture": "Theme - Circadian/Circadian/icon-regex.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_regex",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-regex.png",
        "layer0.tint": {icon_button_on}
    }},
    // Case sensitive search button
    {{
        "class": "icon_case",
        "layer0.texture": "Theme - Circadian/Circadian/icon-case.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_case",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-case.png",
        "layer0.tint": {icon_button_on}
    }},
    // Match whole word search button
    {{
        "class": "icon_whole_word",
        "layer0.texture": "Theme - Circadian/Circadian/icon-word.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_whole_word",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-word.png",
        "layer0.tint": {icon_button_on}
    }},

//
// BOTTOM PANEL ICONS - GROUP 1 (EXTENDED: FIND IN FILES)
//

    // Show search context button
    {{
        "class": "icon_context",
        "layer0.texture": "Theme - Circadian/Circadian/icon-context.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_context",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-context.png",
        "layer0.tint": {icon_button_on}
    }},
    // Use search buffer
    {{
        "class": "icon_use_buffer",
        "layer0.texture": "Theme - Circadian/Circadian/icon-buffer.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_use_buffer",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-buffer.png",
        "layer0.tint": {icon_button_on}
    }},

//
// BOTTOM PANEL ICONS - GROUP 2
//

    // Reverse search direction button
    {{
        "class": "icon_reverse",
        "layer0.texture": "Theme - Circadian/Circadian/icon-reverse.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_reverse",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-reverse.png",
        "layer0.tint": {icon_button_on}
    }},
    // Search wrap button
    {{
        "class": "icon_wrap",
        "layer0.texture": "Theme - Circadian/Circadian/icon-wrap.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_wrap",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-wrap.png",
        "layer0.tint": {icon_button_on}
    }},
    // Search in selection button
    {{
        "class": "icon_in_selection",
        "layer0.texture": "Theme - Circadian/Circadian/icon-selection.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_in_selection",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-selection.png",
        "layer0.tint": {icon_button_on}
    }},

//
// BOTTOM PANEL ICONS - GROUP 3
//

    // Preserve case button
    {{
        "class": "icon_preserve_case",
        "layer0.texture": "Theme - Circadian/Circadian/icon-preserve.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_preserve_case",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-preserve.png",
        "layer0.tint": {icon_button_on}
    }},

//
// BOTTOM PANEL ICONS - GROUP 4
//

    // Highlight results button
    {{
        "class": "icon_highlight",
        "layer0.texture": "Theme - Circadian/Circadian/icon-highlight.png",
        "layer0.opacity": 1.0,
        "layer0.tint": {icon_button_off},
        "content_margin": [8, 8]
    }},
    {{
        "class": "icon_highlight",
        "parents": [{{"class": "icon_button_control", "attributes": ["selected"]}}],
        "layer0.texture": "Theme - Circadian/Circadian/icon-highlight.png",
        "layer0.tint": {icon_button_on}
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

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    @property
    def a(self):
        return self.__a

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
#                                      THEMES
#-------------------------------------------------------------------------------

THEMES = {
    2:  'graveshift',
    6:  'dawn',
    9:  'midday',
    16: 'afternoon',
    18: 'evening',
    21: 'twilight',
}

#-------------------------------------------------------------------------------
#                                       LERP
#-------------------------------------------------------------------------------

import datetime


def lerp_time(func):
    # t = datetime.datetime.now().hour % 24
    t = 2
    t1 = (t + 1) % 24
    # find current theme
    t0 = t
    theme_1 = ''
    while not theme_1:
        if t0 in THEMES:
            theme_1 = THEMES[t0]
        else:
            t0 = (t0 - 1) % 24
    # lerp?
    theme_2 = ''
    lerp = 0.0
    if t1 in THEMES:
        theme_2 = THEMES[t1]
        lerp = datetime.datetime.now().minute / 60.0
    # don't use lerp
    if not theme_2:
        return func(theme_1)
    # lerp me up
    colour_1 = func(theme_1)
    colour_2 = func(theme_2)
    return Colour(
        (colour_1.r * (1.0 - lerp)) + (colour_2.r * lerp),
        (colour_1.g * (1.0 - lerp)) + (colour_2.g * lerp),
        (colour_1.b * (1.0 - lerp)) + (colour_2.b * lerp),
        (colour_1.a * (1.0 - lerp)) + (colour_2.a * lerp)
    )

#-------------------------------------------------------------------------------
#                                   BASE COLOURS
#-------------------------------------------------------------------------------

#-----------------------------------GRAVESHIFT----------------------------------
GRAVESHIFT_BG     = Colour(0.0, 0.0, 0.0)
GRAVESHIFT_ACCENT = Colour(0.0, 1.0, 1.0)
#-------------------------------------MIDDAY------------------------------------
MIDDAY_BG         = Colour(0.78, 0.95, 1.0)
MIDDAY_ACCENT     = Colour(1.0, 0.5, 0.0)
#-----------------------------------AFTERNOON-----------------------------------
AFTERNOON_BG      = Colour(0.98, 0.98, 0.82)
AFTERNOON_ACCENT  = Colour(0.0, 0.65, 0.0)
#------------------------------------EVENING------------------------------------
EVENING_BG        = Colour(0.16, 0.14, 0.14)
EVENING_ACCENT    = Colour(1.0, 0.2, 0.2)
#------------------------------------TWILIGHT-----------------------------------
TWILIGHT_BG       = Colour(0.11, 0.11, 0.11)
TWILIGHT_ACCENT   = Colour(0.6, 0.8, 1.0)

#-------------------------------------------------------------------------------
#                                 COLOUR FUNCTIONS
#-------------------------------------------------------------------------------

#----------------------------------TEXT COLOURS---------------------------------

def get_background(theme):
    if theme == "midday":
        return MIDDAY_BG
    elif theme == 'afternoon':
        return AFTERNOON_BG
    elif theme == 'evening':
        return EVENING_BG
    elif theme == 'twilight':
        return TWILIGHT_BG
    else:
        return GRAVESHIFT_BG

def get_caret(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.1, 0.1, 0.1)
    elif theme == 'evening':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'twilight':
        return Colour(0.95, 0.95, 0.95)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_line_highlight(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.7)
    elif theme == 'afternoon':
        return Colour(0.8, 0.9, 1.0)
    elif theme == 'evening':
        return Colour(0.5, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.2, 0.4, 0.6)
    else:
        return Colour(0.0, 0.0, 0.5)

def get_selection(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.0, 0.9)
    elif theme == 'afternoon':
        return Colour(0.6, 0.8, 1.0, 0.4)
    elif theme == 'evening':
        return Colour(0.6, 0.8, 1.0, 0.6)
    elif theme == 'twilight':
        return Colour(0.5, 0.8, 1.0, 0.6)
    else:
        return Colour(0.7, 0.7, 0.7, 0.3)

def get_inactive_selection(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.0, 0.2)
    elif theme == 'afternoon':
        return Colour(0.6, 0.8, 1.0, 0.2)
    elif theme == 'evening':
        return Colour(0.6, 0.8, 1.0, 0.2)
    elif theme == 'twilight':
        return Colour(0.5, 0.8, 1.0, 0.2)
    else:
        return Colour(0.7, 0.7, 0.7, 0.2)

def get_find_highlight(theme):
    if theme == "midday":
        return Colour(1.0, 0.5, 0.0)
    elif theme == 'afternoon':
        return Colour(0.3, 0.9, 0.3)
    elif theme == 'evening':
        return Colour(0.6, 0.8, 1.0)
    elif theme == 'twilight':
        return Colour(0.8, 0.5, 1.0)
    else:
        return Colour(0.0, 0.7, 1.0)

def get_line_numbers(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'evening':
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'twilight':
        return Colour(0.7, 0.7, 0.7)
    else:
        return Colour(0.0, 0.5, 0.0)

def get_guide(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'evening':
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'twilight':
        return Colour(0.7, 0.7, 0.7)
    else:
        return Colour(0.0, 0.5, 0.0)

def get_comment(theme):
    if theme == "midday":
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'afternoon':
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'evening':
        return Colour(0.45, 0.45, 0.7)
    elif theme == 'twilight':
        return Colour(0.6, 0.5, 0.7)
    else:
        return Colour(0.0, 0.4, 0.0)

def get_literal(theme):
    if theme == "midday":
        return Colour(1.0, 0.05, 0.05)
    elif theme == 'afternoon':
        return Colour(0.3, 0.0, 0.9)
    elif theme == 'evening':
        return Colour(1.0, 0.7, 0.4)
    elif theme == 'twilight':
        return Colour(0.6, 0.8, 1.0)
    else:
        return Colour(1.0, 1.0, 0.0)

def get_string_literal(theme):
    if theme == "midday":
        return Colour(0.0, 0.35, 0.0)
    elif theme == 'afternoon':
        return Colour(0.7, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(1.0, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.4, 0.6, 1.0)
    else:
        return Colour(0.0, 1.0, 1.0)

def get_keyword(theme):
    if theme == "midday":
        return Colour(0.5, 0.0, 0.5)
    elif theme == 'afternoon':
        return Colour(0.0, 0.5, 0.0)
    elif theme == 'evening':
        return Colour(0.4, 0.6, 1.0)
    elif theme == 'twilight':
        return Colour(1.0, 0.6, 1.0)
    else:
        return Colour(0.2, 0.3, 1.0)

def get_entity_name(theme):
    if theme == "midday":
        return Colour(0.3, 0.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.3, 0.2, 0.2)
    elif theme == 'evening':
        return Colour(1.0, 0.2, 0.6)
    elif theme == 'twilight':
        return Colour(0.7, 0.0, 1.0)
    else:
        return Colour(0.6, 0.1, 1.0)

def get_modifier(theme):
    if theme == "midday":
        return Colour(0.8, 0.5, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.4, 0.7)
    elif theme == 'evening':
        return Colour(1.0, 0.3, 0.3)
    elif theme == 'twilight':
        return Colour(0.2, 0.8, 1.0)
    else:
        return Colour(0.3, 1.0, 1.0)

def get_variable(theme):
    if theme == "midday":
        return Colour(0.0, 0.3, 0.2)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.4)
    elif theme == 'evening':
        return Colour(1.0, 0.3, 1.0)
    elif theme == 'twilight':
        return Colour(1.0, 0.4, 0.5)
    else:
        return Colour(1.0, 1.0, 1.0)

def get_builtin_func(theme):
    if theme == "midday":
        return Colour(0.5, 0.0, 0.5)
    elif theme == 'afternoon':
        return Colour(0.0, 0.3, 0.8)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.5)
    elif theme == 'twilight':
        return Colour(1.0, 0.2, 0.2)
    else:
        return Colour(1.0, 0.6, 0.1)

def get_invalid_background(theme):
    if theme == "midday":
        return Colour(1.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(1.0, 0.5, 0.0)
    elif theme == 'evening':
        return Colour(0.0, 1.0, 0.0)
    elif theme == 'twilight':
        return Colour(1.0, 1.0, 0.0)
    else:
        return Colour(1.0, 0.0, 0.0)

def get_invalid_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.0, 0.0, 0.0)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_include_background(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.2, 0.9)
    elif theme == 'evening':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'twilight':
        return Colour(0.4, 0.1, 0.1)
    else:
        return Colour(0.0, 0.0, 0.0, 0.0)

def get_include_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.1, 1.0)
    elif theme == 'afternoon':
        return Colour(1.0, 0.8, 0.0)
    elif theme == 'evening':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.9, 0.9, 0.9)
    else:
        return Colour(0.0, 1.0, 1.0)

#-----------------------------------UI COLOURS----------------------------------

def get_sidebar(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.9, 0.9, 0.9)
    elif theme == 'evening':
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'twilight':
        return Colour(0.15, 0.15, 0.15)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_sb_file_text(theme):
    if theme == "midday":
        return Colour(0.2, 0.2, 0.2)
    elif theme == 'afternoon':
        return Colour(0.1, 0.1, 0.1)
    elif theme == 'evening':
        return Colour(0.1, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.9, 0.9, 0.9)
    else:
        return Colour(0.0, 0.8, 0.0)

def get_sb_folder_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.1, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.9, 0.9, 0.9)
    else:
        return Colour(0.0, 0.8, 0.0)

def get_tab_background(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'evening':
        return Colour(0.34, 0.3, 0.3)
    elif theme == 'twilight':
        return Colour(0.05, 0.05, 0.05)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_tab_active(theme):
    if theme == "midday":
        return Colour(0.85, 0.95, 1.0)
    elif theme == 'afternoon':
        return Colour(0.98, 0.98, 0.82)
    elif theme == 'evening':
        return Colour(0.85, 0.65, 0.3)
    elif theme == 'twilight':
        return Colour(0.45, 0.45, 0.45)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_tab_inactive(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.85, 0.85, 0.85)
    elif theme == 'evening':
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'twilight':
        return Colour(0.25, 0.25, 0.25)
    else:
        return Colour(0.2, 0.2, 0.2)

def get_tab_hover(theme):
    if theme == "midday":
        return Colour(0.9, 0.95, 1.0)
    elif theme == 'afternoon':
        return Colour(1.0, 1.0, 0.94)
    elif theme == 'evening':
        return Colour(0.75, 0.65, 0.5)
    elif theme == 'twilight':
        return Colour(0.35, 0.35, 0.35)
    else:
        return Colour(0.3, 0.3, 0.3)

def get_tab_active_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(1.0, 1.0, 1.0)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_tab_inactive_text(theme):
    if theme == "midday":
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'afternoon':
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'evening':
        return Colour(0.95, 0.95, 0.95)
    elif theme == 'twilight':
        return Colour(0.65, 0.65, 0.65)
    else:
        return Colour(0.8, 0.8, 0.8)

def get_tab_hover_text(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.95, 0.95, 0.95)
    elif theme == 'twilight':
        return Colour(0.8, 0.8, 0.8)
    else:
        return Colour(1.0, 1.0, 1.0)

def get_tab_close(theme):
    if theme == "midday":
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'afternoon':
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'evening':
        return Colour(0.8, 0.8, 0.8)
    elif theme == 'twilight':
        return Colour(0.8, 0.8, 0.8)
    else:
        return Colour(0.6, 0.6, 0.6)

def get_tab_close_hover(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'evening':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'twilight':
        return Colour(1.0, 1.0, 1.0)
    else:
        return Colour(1.0, 1.0, 1.0)

def get_tab_dirty(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_fold_closed(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_fold_closed_pressed(theme):
    if theme == "midday":
        return Colour(1.0, 0.75, 0.25)
    elif theme == 'afternoon':
        return Colour(0.25, 0.85, 0.25)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.5)
    elif theme == 'twilight':
        return Colour(0.8, 1.0, 1.0)
    else:
        return Colour(0.7, 0.7, 0.7)

def get_fold_open(theme):
    if theme == "midday":
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'afternoon':
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'evening':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'twilight':
        return Colour(0.8, 0.8, 0.8)
    else:
        return Colour(0.0, 0.7, 0.0)

def get_fold_open_pressed(theme):
    if theme == "midday":
        return Colour(0.75, 0.75, 0.75)
    elif theme == 'afternoon':
        return Colour(0.75, 0.75, 0.75)
    elif theme == 'evening':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'twilight':
        return Colour(1.0, 1.0, 1.0)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_scroll_bar_background(theme):
    if theme == "midday":
        return Colour(0.88, 0.88, 0.88)
    elif theme == 'afternoon':
        return Colour(0.78, 0.78, 0.78)
    elif theme == 'evening':
        return Colour(0.35, 0.35, 0.35)
    elif theme == 'twilight':
        return Colour(0.2, 0.2, 0.2)
    else:
        return Colour(0.15, 0.15, 0.15)

def get_scroll_bar_corner(theme):
    if theme == "midday":
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'afternoon':
        return Colour(0.65, 0.65, 0.65)
    elif theme == 'evening':
        return Colour(0.3, 0.3, 0.3)
    elif theme == 'twilight':
        return Colour(0.15, 0.15, 0.15)
    else:
        return Colour(0.075, 0.075, 0.075)

def get_scroll_puck(theme):
    if theme == "midday":
        return Colour(0.6, 0.6, 0.6)
    elif theme == 'afternoon':
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'evening':
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'twilight':
        return Colour(0.35, 0.35, 0.35)
    else:
        return Colour(0.3, 0.3, 0.3)

def get_empty_window(theme):
    if theme == "midday":
        return Colour(0.75, 0.75, 0.75)
    elif theme == 'afternoon':
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'evening':
        return Colour(0.14, 0.11, 0.11)
    elif theme == 'twilight':
        return Colour(0.05, 0.0, 0.1)
    else:
        return Colour(0.0, 0.1, 0.0)

def get_layout_divider(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'evening':
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'twilight':
        return Colour(0.45, 0.45, 0.45)
    else:
        return Colour(0.5, 0.5, 0.5)

def get_minimap(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.0, 0.1)
    elif theme == 'afternoon':
        return Colour(0.2, 0.8, 1.0, 0.16)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.0, 0.16)
    elif theme == 'twilight':
        return Colour(0.5, 0.2, 1.0, 0.16)
    else:
        return Colour(0.0, 1.0, 1.0, 0.18)

def get_status_bar(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.35, 0.35, 0.35)
    elif theme == 'evening':
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'twilight':
        return Colour(0.1, 0.1, 0.1)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_status_bar_label(theme):
    if theme == "midday":
        return Colour(0.8, 0.95, 1.0)
    elif theme == 'afternoon':
        return Colour(0.98, 0.98, 0.82)
    elif theme == 'evening':
        return Colour(1.0, 0.8, 0.5)
    elif theme == 'twilight':
        return Colour(0.85, 0.6, 1.0)
    else:
        return Colour(0.0, 0.7, 0.0)

def get_sidebar_selected(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_sidebar_heading(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.37, 0.37, 0.37)
    elif theme == 'evening':
        return Colour(0.72, 0.72, 0.72)
    elif theme == 'twilight':
        return Colour(0.85, 0.85, 0.85)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_sb_file_text_hover(theme):
    if theme == "midday":
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'afternoon':
        return Colour(0.42, 0.42, 0.42)
    elif theme == 'evening':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'twilight':
        return Colour(1.0, 0.8, 1.0)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_sb_file_text_selected(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'evening':
        return Colour(0.96, 0.96, 0.96)
    elif theme == 'twilight':
        return Colour(0.1, 0.1, 0.1)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_sb_folder_icon(theme):
    if theme == "midday":
        return Colour(0.42, 0.42, 0.42)
    elif theme == 'afternoon':
        return Colour(0.42, 0.42, 0.42)
    elif theme == 'evening':
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'twilight':
        return Colour(0.2, 0.4, 0.6)
    else:
        return Colour(0.0, 0.7, 0.7)

def get_sb_folder_icon_hover(theme):
    if theme == "midday":
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'afternoon':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'evening':
        return Colour(0.65, 0.65, 0.65)
    elif theme == 'twilight':
        return Colour(0.4, 0.6, 0.8)
    else:
        return Colour(0.0, 1.0, 1.0)

def get_sb_folder_icon_selected(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'evening':
        return Colour(0.96, 0.96, 0.96)
    elif theme == 'twilight':
        return Colour(0.6, 0.8, 1.0)
    else:
        return Colour(0.0, 1.0, 1.0)

def get_large_button(theme):
    if theme == "midday":
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'afternoon':
        return Colour(0.3, 0.3, 0.3)
    elif theme == 'evening':
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'twilight':
        return Colour(0.14, 0.14, 0.14)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_large_button_pressed(theme):
    if theme == "midday":
        return Colour(0.5, 0.5, 0.5)
    elif theme == 'afternoon':
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'evening':
        return Colour(0.35, 0.35, 0.35)
    elif theme == 'twilight':
        return Colour(0.24, 0.24, 0.24)
    else:
        return Colour(0.2, 0.2, 0.2)

def get_large_button_text(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.9, 0.9, 0.9)
    elif theme == 'evening':
        return Colour(0.8, 0.8, 0.8)
    elif theme == 'twilight':
        return Colour(0.7, 0.7, 0.7)
    else:
        return Colour(0.0, 1.0, 1.0)

def get_panel_background(theme):
    if theme == "midday":
        return Colour(0.65, 0.65, 0.65)
    elif theme == 'afternoon':
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'evening':
        return Colour(0.43, 0.43, 0.43)
    elif theme == 'twilight':
        return Colour(0.3, 0.3, 0.3)
    else:
        return Colour(0.15, 0.15, 0.15)

def get_quick_panel_background(theme):
    if theme == "midday":
        return Colour(0.3, 0.3, 0.3)
    elif theme == 'afternoon':
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'evening':
        return Colour(0.2, 0.2, 0.2)
    elif theme == 'twilight':
        return Colour(0.2, 0.2, 0.2)
    else:
        return Colour(0.1, 0.1, 0.1)

def get_qp_row(theme):
    if theme == "midday":
        return Colour(0.55, 0.55, 0.55)
    elif theme == 'afternoon':
        return Colour(0.45, 0.45, 0.45)
    elif theme == 'evening':
        return Colour(0.35, 0.35, 0.35)
    elif theme == 'twilight':
        return Colour(0.35, 0.35, 0.35)
    else:
        return Colour(0.2, 0.2, 0.2)

def get_qp_row_selected(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_qp_text(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.95, 0.95, 0.95)
    elif theme == 'evening':
        return Colour(0.85, 0.85, 0.85)
    elif theme == 'twilight':
        return Colour(0.85, 0.85, 0.85)
    else:
        return Colour(1.0, 1.0, 1.0)

def get_qp_text_match(theme):
    if theme == "midday":
        return MIDDAY_BG
    elif theme == 'afternoon':
        return AFTERNOON_BG
    elif theme == 'evening':
        return Colour(1.0, 0.6, 0.8)
    elif theme == 'twilight':
        return Colour(1.0, 0.4, 0.4)
    else:
        return Colour(1.0, 0.0, 0.0)

def get_qp_text_selected(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'twilight':
        return Colour(0.0, 0.0, 0.0)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_qp_text_match_selected(theme):
    if theme == "midday":
        return MIDDAY_BG
    elif theme == 'afternoon':
        return AFTERNOON_BG
    elif theme == 'evening':
        return Colour(1.0, 0.6, 0.8)
    elif theme == 'twilight':
        return Colour(1.0, 0.4, 0.4)
    else:
        return Colour(1.0, 0.0, 0.0)

def get_qp_text_score(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.85, 0.95, 1.0)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.25)
    elif theme == 'twilight':
        return Colour(1.0, 0.7, 1.0)
    else:
        return Colour(0.0, 1.0, 0.0)

def get_qp_text_score_selected(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.85, 0.95, 1.0)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.0)
    elif theme == 'twilight':
        return Colour(1.0, 0.2, 1.0)
    else:
        return Colour(0.0, 0.4, 0.0)

def get_ac_background(theme):
    if theme == "midday":
        return Colour(0.45, 0.45, 0.45)
    elif theme == 'afternoon':
        return Colour(0.4, 0.4, 0.4)
    elif theme == 'evening':
        return Colour(0.25, 0.25, 0.25)
    elif theme == 'twilight':
        return Colour(0.25, 0.25, 0.25)
    else:
        return Colour(0.15, 0.15, 0.15)

def get_ac_text(theme):
    if theme == "midday":
        return Colour(1.0, 1.0, 1.0)
    elif theme == 'afternoon':
        return Colour(0.95, 0.95, 0.95)
    elif theme == 'evening':
        return Colour(0.92, 0.92, 0.92)
    elif theme == 'twilight':
        return Colour(0.92, 0.92, 0.92)
    else:
        return Colour(1.0, 1.0, 1.0)

def get_ac_text_match(theme):
    if theme == "midday":
        return MIDDAY_BG
    elif theme == 'afternoon':
        return AFTERNOON_BG
    elif theme == 'evening':
        return Colour(1.0, 0.6, 0.8)
    elif theme == 'twilight':
        return Colour(1.0, 0.4, 0.4)
    else:
        return Colour(1.0, 0.0, 0.0)

def get_ac_text_selected(theme):
    if theme == "midday":
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'afternoon':
        return Colour(0.0, 0.0, 0.0)
    elif theme == 'evening':
        return Colour(0.1, 0.1, 0.1)
    elif theme == 'twilight':
        return Colour(0.1, 0.1, 0.1)
    else:
        return Colour(0.0, 0.0, 0.0)

def get_ac_text_match_selected(theme):
    if theme == "midday":
        return MIDDAY_BG
    elif theme == 'afternoon':
        return AFTERNOON_BG
    elif theme == 'evening':
        return Colour(1.0, 0.6, 0.8)
    elif theme == 'twilight':
        return Colour(1.0, 0.4, 0.4)
    else:
        return Colour(1.0, 0.0, 0.0)

def get_ac_row_selected(theme):
    if theme == "midday":
        return MIDDAY_ACCENT
    elif theme == 'afternoon':
        return AFTERNOON_ACCENT
    elif theme == 'evening':
        return EVENING_ACCENT
    elif theme == 'twilight':
        return TWILIGHT_ACCENT
    else:
        return GRAVESHIFT_ACCENT

def get_icon_button_off(theme):
    if theme == "midday":
        return Colour(0.75, 0.75, 0.75)
    elif theme == 'afternoon':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'evening':
        return Colour(0.7, 0.7, 0.7)
    elif theme == 'twilight':
        return Colour(0.6, 0.6, 0.6)
    else:
        return Colour(0.5, 0.5, 0.5)

def get_icon_button_on(theme):
    if theme == "midday":
        return Colour(0.9, 0.9, 0.0)
    elif theme == 'afternoon':
        return Colour(0.65, 0.85, 1.0)
    elif theme == 'evening':
        return Colour(1.0, 0.5, 0.25)
    elif theme == 'twilight':
        return Colour(1.0, 0.7, 1.0)
    else:
        return GRAVESHIFT_ACCENT

#-------------------------------------------------------------------------------
#                             APPLY COLOURS AND WRITE
#-------------------------------------------------------------------------------

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
        background=lerp_time(get_background).to_hex(),
        caret=lerp_time(get_caret).to_hex(),
        text=lerp_time(get_text).to_hex(),
        line_highlight=lerp_time(get_line_highlight).to_hex(),
        selection=lerp_time(get_selection).to_hex(),
        inactive_selection=lerp_time(get_inactive_selection).to_hex(),
        find_highlight=lerp_time(get_find_highlight).to_hex(),
        line_numbers=lerp_time(get_line_numbers).to_hex(),
        guide=lerp_time(get_guide).to_hex(),
        comment=lerp_time(get_comment).to_hex(),
        literal=lerp_time(get_literal).to_hex(),
        string_literal=lerp_time(get_string_literal).to_hex(),
        keyword=lerp_time(get_keyword).to_hex(),
        entity_name=lerp_time(get_entity_name).to_hex(),
        modifier=lerp_time(get_modifier).to_hex(),
        variable=lerp_time(get_variable).to_hex(),
        builtin_func=lerp_time(get_builtin_func).to_hex(),
        invalid_background=lerp_time(get_invalid_background).to_hex(),
        invalid_text=lerp_time(get_invalid_text).to_hex(),
        include_background=lerp_time(get_include_background).to_hex(),
        include_text=lerp_time(get_include_text).to_hex()
    ))

# write the ui theme
with open(UI_THEME_PATH, 'w') as f:
    f.write(UI_THEME_DATA.format(
        sidebar=lerp_time(get_sidebar).to_tuple(),
        sb_file_text=lerp_time(get_sb_file_text).to_tuple(),
        sb_folder_text=lerp_time(get_sb_folder_text).to_tuple(),
        tab_background=lerp_time(get_tab_background).to_tuple(),
        tab_active=lerp_time(get_tab_active).to_tuple(),
        tab_inactive=lerp_time(get_tab_inactive).to_tuple(),
        tab_hover=lerp_time(get_tab_hover).to_tuple(),
        tab_active_text=lerp_time(get_tab_active_text).to_tuple(),
        tab_inactive_text=lerp_time(get_tab_inactive_text).to_tuple(),
        tab_hover_text=lerp_time(get_tab_hover_text).to_tuple(),
        tab_close=lerp_time(get_tab_close).to_tuple(),
        tab_close_hover=lerp_time(get_tab_close_hover).to_tuple(),
        tab_dirty=lerp_time(get_tab_dirty).to_tuple(),
        fold_closed=lerp_time(get_fold_closed).to_tuple(),
        fold_closed_pressed=lerp_time(get_fold_closed_pressed).to_tuple(),
        fold_open=lerp_time(get_fold_open).to_tuple(),
        fold_open_pressed=lerp_time(get_fold_open_pressed).to_tuple(),
        scroll_bar_background=lerp_time(get_scroll_bar_background).to_tuple(),
        scroll_bar_corner=lerp_time(get_scroll_bar_corner).to_tuple(),
        scroll_puck=lerp_time(get_scroll_puck).to_tuple(),
        empty_window=lerp_time(get_empty_window).to_tuple(),
        layout_divider=lerp_time(get_layout_divider).to_tuple(),
        minimap=lerp_time(get_minimap).to_tuple(),
        status_bar=lerp_time(get_status_bar).to_tuple(),
        status_bar_label=lerp_time(get_status_bar_label).to_tuple(),
        sidebar_selected=lerp_time(get_sidebar_selected).to_tuple(),
        sidebar_heading=lerp_time(get_sidebar_heading).to_tuple(),
        sb_file_text_hover=lerp_time(get_sb_file_text_hover).to_tuple(),
        sb_file_text_selected=lerp_time(get_sb_file_text_selected).to_tuple(),
        sb_folder_icon=lerp_time(get_sb_folder_icon).to_tuple(),
        sb_folder_icon_hover=lerp_time(get_sb_folder_icon_hover).to_tuple(),
        sb_folder_icon_selected=lerp_time(get_sb_folder_icon_selected).to_tuple(),
        large_button=lerp_time(get_large_button).to_tuple(),
        large_button_pressed=lerp_time(get_large_button_pressed).to_tuple(),
        large_button_text=lerp_time(get_large_button_text).to_tuple(),
        panel_background=lerp_time(get_panel_background).to_tuple(),
        quick_panel_background=lerp_time(get_quick_panel_background).to_tuple(),
        qp_row=lerp_time(get_qp_row).to_tuple(),
        qp_row_selected=lerp_time(get_qp_row_selected).to_tuple(),
        qp_text=lerp_time(get_qp_text).to_tuple(),
        qp_text_match=lerp_time(get_qp_text_match).to_tuple(),
        qp_text_selected=lerp_time(get_qp_text_selected).to_tuple(),
        qp_text_match_selected=lerp_time(get_qp_text_match_selected).to_tuple(),
        qp_text_score=lerp_time(get_qp_text_score).to_tuple(),
        qp_text_score_selected=lerp_time(get_qp_text_score_selected).to_tuple(),
        ac_background=lerp_time(get_ac_background).to_tuple(),
        ac_text=lerp_time(get_ac_text).to_tuple(),
        ac_text_match=lerp_time(get_ac_text_match).to_tuple(),
        ac_text_selected=lerp_time(get_ac_text_selected).to_tuple(),
        ac_text_match_selected=lerp_time(get_ac_text_match_selected).to_tuple(),
        ac_row_selected=lerp_time(get_ac_row_selected).to_tuple(),
        icon_button_off=lerp_time(get_icon_button_off).to_tuple(),
        icon_button_on=lerp_time(get_icon_button_on).to_tuple()
    ))
