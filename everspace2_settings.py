
""" This is an compacted example of the Everspace 2 game's settings GUI. """

import json
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QWidget
)
from PyQt5.uic import loadUi


class SettingsGUI(QMainWindow):
    """ Implements Everspace 2 GUI example. """
    def __init__(self):
        super(SettingsGUI, self).__init__()

        # Sets UI file
        self.script_directory = os.path.realpath(__file__)
        self.script_directory = os.path.dirname(self.script_directory)
        ui_file = self.script_directory + '/ui/settings.ui'
        widget = loadUi(ui_file)
        self.setCentralWidget(widget)

        # Variables for widgets to be used later
        self.gamma_progress_bar = None
        self.decrease_gamma_button = None
        self.gamma_value_label = None
        self.increase_gamma_button = None
        self.toggle_previous_deficiency_mode_button = None
        self.deficiency_mode_value_label = None
        self.toggle_next_deficiency_mode_button = None
        self.toggle_previous_motion_blur_button = None
        self.motion_blur_value_label = None
        self.toggle_next_motion_blur_button = None
        self.toggle_previous_chromatic_aberration_button = None
        self.chromatic_aberration_value_label = None
        self.toggle_next_chromatic_aberration_button = None
        self.toggle_previous_lens_flares_button = None
        self.lens_flares_value_label = None
        self.toggle_next_lens_flares_button = None
        self.master_progress_bar = None
        self.decrease_master_button = None
        self.master_value_label = None
        self.increase_master_button = None
        self.apply_settings_button = None
        self.music_progress_bar = None
        self.decrease_music_button = None
        self.music_value_label = None
        self.increase_music_button = None
        self.sfx_progress_bar = None
        self.decrease_sfx_button = None
        self.sfx_value_label = None
        self.increase_sfx_button = None
        self.atmo_progress_bar = None
        self.decrease_atmo_button = None
        self.atmo_value_label = None
        self.increase_atmo_button = None
        self.voice_progress_bar = None
        self.decrease_voice_button = None
        self.voice_value_label = None
        self.increase_voice_button = None
        self.background_chatter_progress_bar = None
        self.decrease_background_chatter_button = None
        self.background_chatter_value_label = None
        self.increase_background_chatter_button = None
        self.video_progress_bar = None
        self.decrease_video_button = None
        self.video_value_label = None
        self.increase_video_button = None
        self.wireless_controller_speaker_progress_bar = None
        self.decrease_wireless_controller_speaker_button = None
        self.wireless_controller_speaker_value_label = None
        self.increase_wireless_controller_speaker_button = None
        self.toggle_previous_spoken_language_button = None
        self.spoken_language_value_label = None
        self.toggle_next_spoken_language_button = None
        self.toggle_previous_input_smoothing_button = None
        self.input_smoothing_value_label = None
        self.toggle_next_input_smoothing_button = None
        self.auto_aiming_strength_progress_bar = None
        self.toggle_previous_auto_aiming_strength_button = None
        self.auto_aiming_strength_value_label = None
        self.toggle_next_auto_aiming_strength_button = None
        self.toggle_previous_pitch_input_button = None
        self.pitch_input_value_label = None
        self.toggle_next_pitch_input_button = None
        self.toggle_previous_yaw_input_button = None
        self.yaw_input_value_label = None
        self.toggle_next_yaw_input_button = None
        self.toggle_previous_roll_input_button = None
        self.roll_input_value_label = None
        self.toggle_next_roll_input_button = None
        self.toggle_previous_camera_pitch_input_button = None
        self.camera_pitch_input_value_label = None
        self.toggle_next_camera_pitch_input_button = None
        self.toggle_previous_camera_yaw_input_button = None
        self.camera_yaw_input_value_label = None
        self.toggle_next_camera_yaw_input_button = None
        self.toggle_previous_difficulty_button = None
        self.difficulty_value_label = None
        self.toggle_next_difficulty_button = None
        self.toggle_previous_auto_saving_base_button = None
        self.auto_saving_base_value_label = None
        self.toggle_next_auto_saving_base_button = None
        self.toggle_previous_slow_down_time_button = None
        self.slow_down_time_value_label = None
        self.toggle_next_slow_down_time_button = None
        self.toggle_previous_inertia_button_mode_button = None
        self.inertia_button_mode_value_label = None
        self.toggle_next_inertia_button_mode_button = None
        self.toggle_previous_show_damage_numbers_button = None
        self.show_damage_numbers_value_label = None
        self.toggle_next_show_damage_numbers_button = None
        self.toggle_previous_show_xp_numbers_button = None
        self.show_xp_numbers_value_label = None
        self.toggle_next_show_xp_numbers_button = None
        self.toggle_previous_show_cockpit_hud_button = None
        self.show_cockpit_hud_value_label = None
        self.toggle_next_show_cockpit_hud_button = None
        self.markers_icons_group_box = None
        self.toggle_previous_markers_color_button = None
        self.markers_color_value_label = None
        self.toggle_next_markers_color_button = None

        self.settings_file = self.script_directory + '/bin/settings.json'
        self.decimal_number_step = 0.05
        self.whole_number_step = 5
        self.color_vision_deficiency_modes = (
            'Off', 'Deuteranope', 'Protanope', 'Tritanope')
        self.on_off_values = ('On', 'Off')
        self.spoken_languages = ('English', 'German')
        self.inverted_options = ('Not Inverted', 'Inverted')
        self.difficulties = (
            'Very Easy', 'Easy', 'Normal', 'Hard', 'Very Hard')
        self.auto_save_bases = ('Enabled', 'Time-based only',
                                'Collectible-based only', 'Disabled')
        self.slow_time_options = ('Enabled', 'Disabled')
        self.inertia_button_modes = ('Toggle', 'Hold To Enable')
        self.show_hide_options = ('Show', 'Hide')
        self.marker_colors = ('White', 'Blue', 'Red', 'Yellow', 'Green')

        self.set_widgets()
        self.set_callbacks()
        self.set_marker_icons()
        self.load_settings()

    def set_widgets(self):
        """ Finds and sets widgets as configured in the .ui file. """

        self.gamma_progress_bar = self.findChild(
            QProgressBar, 'gamma_progress_bar')
        self.decrease_gamma_button = self.findChild(
            QPushButton, 'decrease_gamma_button')
        self.gamma_value_label = self.findChild(QLabel, 'gamma_value_label')
        self.increase_gamma_button = self.findChild(
            QPushButton, 'increase_gamma_button')

        self.toggle_previous_deficiency_mode_button = self.findChild(
            QPushButton, 'toggle_previous_deficiency_mode_button')
        self.deficiency_mode_value_label = self.findChild(
            QLabel, 'deficiency_mode_value_label')
        self.toggle_next_deficiency_mode_button = self.findChild(
            QPushButton, 'toggle_next_deficiency_mode_button')

        self.toggle_previous_motion_blur_button = self.findChild(
            QPushButton, 'toggle_previous_motion_blur_button')
        self.motion_blur_value_label = self.findChild(
            QLabel, 'motion_blur_value_label')
        self.toggle_next_motion_blur_button = self.findChild(
            QPushButton, 'toggle_next_motion_blur_button')

        self.toggle_previous_chromatic_aberration_button = self.findChild(
            QPushButton, 'toggle_previous_chromatic_aberration_button')
        self.chromatic_aberration_value_label = self.findChild(
            QLabel, 'chromatic_aberration_value_label')
        self.toggle_next_chromatic_aberration_button = self.findChild(
            QPushButton, 'toggle_next_chromatic_aberration_button')

        self.toggle_previous_lens_flares_button = self.findChild(
            QPushButton, 'toggle_previous_lens_flares_button')
        self.lens_flares_value_label = self.findChild(
            QLabel, 'lens_flares_value_label')
        self.toggle_next_lens_flares_button = self.findChild(
            QPushButton, 'toggle_next_lens_flares_button')

        self.master_progress_bar = self.findChild(
            QProgressBar, 'master_progress_bar')
        self.decrease_master_button = self.findChild(
            QPushButton, 'decrease_master_button')
        self.master_value_label = self.findChild(QLabel, 'master_value_label')
        self.increase_master_button = self.findChild(
            QPushButton, 'increase_master_button')

        self.music_progress_bar = self.findChild(
            QProgressBar, 'music_progress_bar')
        self.decrease_music_button = self.findChild(
            QPushButton, 'decrease_music_button')
        self.music_value_label = self.findChild(QLabel, 'music_value_label')
        self.increase_music_button = self.findChild(
            QPushButton, 'increase_music_button')

        self.sfx_progress_bar = self.findChild(
            QProgressBar, 'sfx_progress_bar')
        self.decrease_sfx_button = self.findChild(
            QPushButton, 'decrease_sfx_button')
        self.sfx_value_label = self.findChild(QLabel, 'sfx_value_label')
        self.increase_sfx_button = self.findChild(
            QPushButton, 'increase_sfx_button')

        self.atmo_progress_bar = self.findChild(
            QProgressBar, 'atmo_progress_bar')
        self.decrease_atmo_button = self.findChild(
            QPushButton, 'decrease_atmo_button')
        self.atmo_value_label = self.findChild(QLabel, 'atmo_value_label')
        self.increase_atmo_button = self.findChild(
            QPushButton, 'increase_atmo_button')

        self.voice_progress_bar = self.findChild(
            QProgressBar, 'voice_progress_bar')
        self.decrease_voice_button = self.findChild(
            QPushButton, 'decrease_voice_button')
        self.voice_value_label = self.findChild(QLabel, 'voice_value_label')
        self.increase_voice_button = self.findChild(
            QPushButton, 'increase_voice_button')

        self.background_chatter_progress_bar = self.findChild(
            QProgressBar, 'background_chatter_progress_bar')
        self.decrease_background_chatter_button = self.findChild(
            QPushButton, 'decrease_background_chatter_button')
        self.background_chatter_value_label = self.findChild(
            QLabel, 'background_chatter_value_label')
        self.increase_background_chatter_button = self.findChild(
            QPushButton, 'increase_background_chatter_button')

        self.video_progress_bar = self.findChild(
            QProgressBar, 'video_progress_bar')
        self.decrease_video_button = self.findChild(
            QPushButton, 'decrease_video_button')
        self.video_value_label = self.findChild(QLabel, 'video_value_label')
        self.increase_video_button = self.findChild(
            QPushButton, 'increase_video_button')

        self.wireless_controller_speaker_progress_bar = self.findChild(
            QProgressBar, 'wireless_controller_speaker_progress_bar')
        self.decrease_wireless_controller_speaker_button = self.findChild(
            QPushButton, 'decrease_wireless_controller_speaker_button')
        self.wireless_controller_speaker_value_label = self.findChild(
            QLabel, 'wireless_controller_speaker_value_label')
        self.increase_wireless_controller_speaker_button = self.findChild(
            QPushButton, 'increase_wireless_controller_speaker_button')

        self.toggle_previous_spoken_language_button = self.findChild(
            QPushButton, 'toggle_previous_spoken_language_button')
        self.spoken_language_value_label = self.findChild(
            QLabel, 'spoken_language_value_label')
        self.toggle_next_spoken_language_button = self.findChild(
            QPushButton, 'toggle_next_spoken_language_button')

        self.toggle_previous_input_smoothing_button = self.findChild(
            QPushButton, 'toggle_previous_input_smoothing_button')
        self.input_smoothing_value_label = self.findChild(
            QLabel, 'input_smoothing_value_label')
        self.toggle_next_input_smoothing_button = self.findChild(
            QPushButton, 'toggle_next_input_smoothing_button')

        self.auto_aiming_strength_progress_bar = self.findChild(
            QProgressBar, 'auto_aiming_strength_progress_bar')
        self.toggle_previous_auto_aiming_strength_button = self.findChild(
            QPushButton, 'toggle_previous_auto_aiming_strength_button')
        self.auto_aiming_strength_value_label = self.findChild(
            QLabel, 'auto_aiming_strength_value_label')
        self.toggle_next_auto_aiming_strength_button = self.findChild(
            QPushButton, 'toggle_next_auto_aiming_strength_button')

        self.toggle_previous_pitch_input_button = self.findChild(
            QPushButton, 'toggle_previous_pitch_input_button')
        self.pitch_input_value_label = self.findChild(
            QLabel, 'pitch_input_value_label')
        self.toggle_next_pitch_input_button = self.findChild(
            QPushButton, 'toggle_next_pitch_input_button')

        self.toggle_previous_yaw_input_button = self.findChild(
            QPushButton, 'toggle_previous_yaw_input_button')
        self.yaw_input_value_label = self.findChild(
            QLabel, 'yaw_input_value_label')
        self.toggle_next_yaw_input_button = self.findChild(
            QPushButton, 'toggle_next_yaw_input_button')

        self.toggle_previous_roll_input_button = self.findChild(
            QPushButton, 'toggle_previous_roll_input_button')
        self.roll_input_value_label = self.findChild(
            QLabel, 'roll_input_value_label')
        self.toggle_next_roll_input_button = self.findChild(
            QPushButton, 'toggle_next_roll_input_button')

        self.toggle_previous_camera_pitch_input_button = self.findChild(
            QPushButton, 'toggle_previous_camera_pitch_input_button')
        self.camera_pitch_input_value_label = self.findChild(
            QLabel, 'camera_pitch_input_value_label')
        self.toggle_next_camera_pitch_input_button = self.findChild(
            QPushButton, 'toggle_next_camera_pitch_input_button')

        self.toggle_previous_camera_yaw_input_button = self.findChild(
            QPushButton, 'toggle_previous_camera_yaw_input_button')
        self.camera_yaw_input_value_label = self.findChild(
            QLabel, 'camera_yaw_input_value_label')
        self.toggle_next_camera_yaw_input_button = self.findChild(
            QPushButton, 'toggle_next_camera_yaw_input_button')

        self.toggle_previous_difficulty_button = self.findChild(
            QPushButton, 'toggle_previous_difficulty_button')
        self.difficulty_value_label = self.findChild(
            QLabel, 'difficulty_value_label')
        self.toggle_next_difficulty_button = self.findChild(
            QPushButton, 'toggle_next_difficulty_button')

        self.toggle_previous_auto_saving_base_button = self.findChild(
            QPushButton, 'toggle_previous_auto_saving_base_button')
        self.auto_saving_base_value_label = self.findChild(
            QLabel, 'auto_saving_base_value_label')
        self.toggle_next_auto_saving_base_button = self.findChild(
            QPushButton, 'toggle_next_auto_saving_base_button')

        self.toggle_previous_slow_down_time_button = self.findChild(
            QPushButton, 'toggle_previous_slow_down_time_button')
        self.slow_down_time_value_label = self.findChild(
            QLabel, 'slow_down_time_value_label')
        self.toggle_next_slow_down_time_button = self.findChild(
            QPushButton, 'toggle_next_slow_down_time_button')

        self.toggle_previous_inertia_button_mode_button = self.findChild(
            QPushButton, 'toggle_previous_inertia_button_mode_button')
        self.inertia_button_mode_value_label = self.findChild(
            QLabel, 'inertia_button_mode_value_label')
        self.toggle_next_inertia_button_mode_button = self.findChild(
            QPushButton, 'toggle_next_inertia_button_mode_button')

        self.toggle_previous_show_damage_numbers_button = self.findChild(
            QPushButton, 'toggle_previous_show_damage_numbers_button')
        self.show_damage_numbers_value_label = self.findChild(
            QLabel, 'show_damage_numbers_value_label')
        self.toggle_next_show_damage_numbers_button = self.findChild(
            QPushButton, 'toggle_next_show_damage_numbers_button')

        self.toggle_previous_show_xp_numbers_button = self.findChild(
            QPushButton, 'toggle_previous_show_xp_numbers_button')
        self.show_xp_numbers_value_label = self.findChild(
            QLabel, 'show_xp_numbers_value_label')
        self.toggle_next_show_xp_numbers_button = self.findChild(
            QPushButton, 'toggle_next_show_xp_numbers_button')

        self.toggle_previous_show_cockpit_hud_button = self.findChild(
            QPushButton, 'toggle_previous_show_cockpit_hud_button')
        self.show_cockpit_hud_value_label = self.findChild(
            QLabel, 'show_cockpit_hud_value_label')
        self.toggle_next_show_cockpit_hud_button = self.findChild(
            QPushButton, 'toggle_next_show_cockpit_hud_button')

        self.markers_icons_group_box = self.findChild(
            QGroupBox, 'markers_icons_group_box')
        self.toggle_previous_markers_color_button = self.findChild(
            QPushButton, 'toggle_previous_markers_color_button')
        self.markers_color_value_label = self.findChild(
            QLabel, 'markers_color_value_label')
        self.toggle_next_markers_color_button = self.findChild(
            QPushButton, 'toggle_next_markers_color_button')

        self.apply_settings_button = self.findChild(
            QPushButton, 'apply_settings_button')

    def set_callbacks(self):
        """ Sets callbacks to widgets. """

        self.decrease_gamma_button.clicked.connect(
            lambda: self.change_decimal_number_value(
                self.gamma_value_label, self.gamma_progress_bar, -1))

        self.increase_gamma_button.clicked.connect(
            lambda: self.change_decimal_number_value(
                self.gamma_value_label, self.gamma_progress_bar, 1))

        self.toggle_previous_deficiency_mode_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.deficiency_mode_value_label,
                self.color_vision_deficiency_modes,
                -1
            )
        )

        self.toggle_next_deficiency_mode_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.deficiency_mode_value_label,
                self.color_vision_deficiency_modes,
                1
            )
        )

        self.toggle_previous_motion_blur_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.motion_blur_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_motion_blur_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.motion_blur_value_label,
                self.on_off_values,
                1
            )
        )

        self.toggle_previous_chromatic_aberration_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.chromatic_aberration_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_chromatic_aberration_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.chromatic_aberration_value_label,
                self.on_off_values,
                1
            )
        )

        self.toggle_previous_lens_flares_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.lens_flares_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_lens_flares_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.lens_flares_value_label,
                self.on_off_values,
                1
            )
        )

        self.decrease_master_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.master_value_label, self.master_progress_bar, -1))

        self.increase_master_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.master_value_label, self.master_progress_bar, 1))

        self.decrease_music_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.music_value_label, self.music_progress_bar, -1))

        self.increase_music_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.music_value_label, self.music_progress_bar, 1))

        self.decrease_sfx_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.sfx_value_label, self.sfx_progress_bar, -1))

        self.increase_sfx_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.sfx_value_label, self.sfx_progress_bar, 1))

        self.decrease_atmo_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.atmo_value_label, self.atmo_progress_bar, -1))

        self.increase_atmo_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.atmo_value_label, self.atmo_progress_bar, 1))

        self.decrease_voice_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.voice_value_label, self.voice_progress_bar, -1))

        self.increase_voice_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.voice_value_label, self.voice_progress_bar, 1))

        self.decrease_background_chatter_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.background_chatter_value_label,
                self.background_chatter_progress_bar,
                -1
            )
        )

        self.increase_background_chatter_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.background_chatter_value_label,
                self.background_chatter_progress_bar,
                1
            )
        )

        self.decrease_video_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.video_value_label,
                self.video_progress_bar,
                -1
            )
        )

        self.increase_video_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.video_value_label,
                self.video_progress_bar,
                1
            )
        )

        self.decrease_wireless_controller_speaker_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.wireless_controller_speaker_value_label,
                self.wireless_controller_speaker_progress_bar,
                -1
            )
        )

        self.increase_wireless_controller_speaker_button.clicked.connect(
            lambda: self.change_whole_number_value(
                self.wireless_controller_speaker_value_label,
                self.wireless_controller_speaker_progress_bar,
                1
            )
        )

        self.toggle_previous_spoken_language_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.spoken_language_value_label,
                self.spoken_languages,
                -1
            )
        )

        self.toggle_next_spoken_language_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.spoken_language_value_label,
                self.spoken_languages,
                1
            )
        )

        self.toggle_previous_input_smoothing_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.input_smoothing_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_input_smoothing_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.input_smoothing_value_label,
                self.on_off_values,
                1
            )
        )

        self.toggle_previous_auto_aiming_strength_button.clicked.connect(
            lambda: self.change_decimal_number_value(
                self.auto_aiming_strength_value_label,
                self.auto_aiming_strength_progress_bar,
                -1
            )
        )

        self.toggle_next_auto_aiming_strength_button.clicked.connect(
            lambda: self.change_decimal_number_value(
                self.auto_aiming_strength_value_label,
                self.auto_aiming_strength_progress_bar,
                1
            )
        )

        self.toggle_previous_pitch_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.pitch_input_value_label,
                self.inverted_options,
                -1
            )
        )

        self.toggle_next_pitch_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.pitch_input_value_label,
                self.inverted_options,
                1
            )
        )

        self.toggle_previous_yaw_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.yaw_input_value_label,
                self.inverted_options,
                -1
            )
        )

        self.toggle_next_yaw_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.yaw_input_value_label,
                self.inverted_options,
                1
            )
        )

        self.toggle_previous_roll_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.roll_input_value_label,
                self.inverted_options,
                -1
            )
        )

        self.toggle_next_roll_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.roll_input_value_label,
                self.inverted_options,
                1
            )
        )

        self.toggle_previous_camera_pitch_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.camera_pitch_input_value_label,
                self.inverted_options,
                -1
            )
        )

        self.toggle_next_camera_pitch_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.camera_pitch_input_value_label,
                self.inverted_options,
                1
            )
        )

        self.toggle_previous_camera_yaw_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.camera_yaw_input_value_label,
                self.inverted_options,
                -1
            )
        )

        self.toggle_next_camera_yaw_input_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.camera_yaw_input_value_label,
                self.inverted_options,
                1
            )
        )

        self.toggle_previous_difficulty_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.difficulty_value_label,
                self.difficulties,
                -1
            )
        )

        self.toggle_next_difficulty_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.difficulty_value_label,
                self.difficulties,
                1
            )
        )

        self.toggle_previous_auto_saving_base_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.auto_saving_base_value_label,
                self.auto_save_bases,
                -1
            )
        )

        self.toggle_next_auto_saving_base_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.auto_saving_base_value_label,
                self.auto_save_bases,
                1
            )
        )

        self.toggle_previous_slow_down_time_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.slow_down_time_value_label,
                self.slow_time_options,
                -1
            )
        )

        self.toggle_next_slow_down_time_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.slow_down_time_value_label,
                self.slow_time_options,
                1
            )
        )

        self.toggle_previous_inertia_button_mode_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.inertia_button_mode_value_label,
                self.inertia_button_modes,
                -1
            )
        )

        self.toggle_next_inertia_button_mode_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.inertia_button_mode_value_label,
                self.inertia_button_modes,
                1
            )
        )

        self.toggle_previous_show_damage_numbers_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_damage_numbers_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_show_damage_numbers_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_damage_numbers_value_label,
                self.on_off_values,
                1
            )
        )

        self.toggle_previous_show_xp_numbers_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_xp_numbers_value_label,
                self.on_off_values,
                -1
            )
        )

        self.toggle_next_show_xp_numbers_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_xp_numbers_value_label,
                self.on_off_values,
                1
            )
        )

        self.toggle_previous_show_cockpit_hud_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_cockpit_hud_value_label,
                self.show_hide_options,
                -1
            )
        )

        self.toggle_next_show_cockpit_hud_button.clicked.connect(
            lambda: self.toggle_widget_options(
                self.show_cockpit_hud_value_label,
                self.show_hide_options,
                1
            )
        )

        self.toggle_previous_markers_color_button.clicked.connect(
            lambda: self.toggle_marker_color(-1))
        self.toggle_next_markers_color_button.clicked.connect(
            lambda: self.toggle_marker_color(1))

        self.apply_settings_button.clicked.connect(self.apply_settings)

    def set_marker_icons(self):
        """ Sets markers' icons in the Game -> Display section. """

        icons_directory = self.script_directory + '/icons'
        icons_files = os.listdir(icons_directory)

        icon_labels = self.markers_icons_group_box.findChildren(QLabel)
        for file_name, icon_label in zip(icons_files, icon_labels):
            icon_file = icons_directory + '/' + file_name
            pixmap = QPixmap(icon_file)
            scaled_pixmap = pixmap.scaled(
                32, 32,
                aspectRatioMode=Qt.KeepAspectRatio,
                transformMode=Qt.SmoothTransformation
            )

            colored_pixmap = self.set_icon_color(scaled_pixmap)
            icon_label.setPixmap(colored_pixmap)

    def set_icon_color(self, pixmap: QPixmap) -> QPixmap:
        """ Sets given icon's pixmap color according to a color selected
        in the GUI.

        Parameters:
            pixmap - An object that handles icon's color and size.

        Returns:
            colored_pixmap - A colored pixmap object.
        """

        colored_pixmap = QPixmap(pixmap.size())

        # Fill with transparent color
        colored_pixmap.fill(QColor('transparent'))

        # Create a QPainter to draw on the new pixmap
        painter = QPainter(colored_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)  # Draw the original pixmap
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)

        # Fills icon with a desired color
        color = self.markers_color_value_label.text()
        painter.fillRect(colored_pixmap.rect(), QColor(color.lower()))
        painter.end()

        return colored_pixmap

    def change_decimal_number_value(self, widget: QWidget,
                                    progress_widget: QWidget, direction: int):
        """ Changes given widget's value in decimal number steps in the
        GUI.

        Parameters:
            widget - The widget which value to change.
            progress_widget - The progress bar widget to show the change.
            direction - sign value of the change's direction.
        """

        value = float(widget.text())
        value = round(value + (direction * self.decimal_number_step), 2)
        if value >= 0 and value <= 1:
            widget.setText(str(value))

            max_value = progress_widget.maximum()
            value = int(max_value * value)
            progress_widget.setValue(value)

    def change_whole_number_value(self, widget: QWidget,
                                  progress_widget: QWidget, direction: int):
        """ Changes given widget's value in whole number steps in the
        GUI.

        Parameters:
            widget - The widget which value to change.
            progress_widget - The progress bar widget to show the change.
            direction - sign value of the change's direction.
        """

        value = int(widget.text())
        value = value + (direction * self.whole_number_step)
        if value >= 0 and value <= 100:
            widget.setText(str(value))

            max_value = progress_widget.maximum()
            value = int(max_value * value/100)
            progress_widget.setValue(value)

    def toggle_widget_options(self, widget: QWidget, options: tuple,
                              direction: int):
        """ Changes given widget's option value in the GUI.

        Parameters:
            widget - The widget which value to change
            options - A tuple with widget's options
            direction - sign value of the change's direction
        """
        value = widget.text()
        index = options.index(value)
        index += direction
        if index >= len(options):
            index = 0

        value = options[index]
        widget.setText(value)

    def toggle_marker_color(self, direction: int):
        """ Toggle markers color option in the GUI. """

        self.toggle_widget_options(
            self.markers_color_value_label, self.marker_colors, direction)
        self.set_marker_icons()

    def load_settings(self):
        """ Loads settings from a .json file. """

        with open(self.settings_file, encoding='utf-8') as file:
            data = json.load(file)
            for widget_name, value in data.items():
                widget = self.findChildren((QLabel, QProgressBar),
                                           name=widget_name)
                if widget:
                    widget = widget[0]
                    if isinstance(widget, QLabel):
                        widget.setText(value)
                        if widget.objectName() == 'markers_color_value_label':
                            self.set_marker_icons()
                    elif isinstance(widget, QProgressBar):
                        widget.setValue(value)

    def apply_settings(self):
        """ Saves the settings into the settings.json file. """

        data = {}
        group_boxes = self.findChildren(QGroupBox)
        for group_box in group_boxes:
            widgets = group_box.children()
            for widget in widgets:
                widget_name = widget.objectName()
                if isinstance(widget, QLabel):
                    data[widget_name] = widget.text()
                elif isinstance(widget, QProgressBar):
                    data[widget_name] = widget.value()

        with open(self.settings_file, 'w', encoding='utf-8') as file:
            json.dump(data, file)

        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText('Applied the settings successfully!')
        message_box.setWindowTitle('Applying Settings')
        message_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SettingsGUI()
    window.show()
    sys.exit(app.exec_())
