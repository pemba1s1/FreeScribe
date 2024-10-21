"""
SettingsWindowUI Module

This module provides a user interface for managing application settings.
It includes a class `SettingsWindowUI` that handles the creation and management
of a settings window using Tkinter.

This software is released under the AGPL-3.0 license
Copyright (c) 2023-2024 Braedon Hendy

Further updates and packaging added in 2024 through the ClinicianFOCUS initiative, 
a collaboration with Dr. Braedon Hendy and Conestoga College Institute of Applied 
Learning and Technology as part of the CNERG+ applied research project, 
Unburdening Primary Healthcare: An Open-Source AI Clinician Partner Platform". 
Prof. Michael Yingbull (PI), Dr. Braedon Hendy (Partner), 
and Research Students - Software Developer Alex Simko, Pemba Sherpa (F24), and Naitik Patel.

Classes:
    SettingsWindowUI: Manages the settings window UI.
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
import Tooltip as tt


class SettingsWindowUI:
    """
    Manages the settings window UI.

    This class creates and manages a settings window using Tkinter. It includes
    methods to open the settings window, create various settings frames, and
    handle user interactions such as saving settings.

    Attributes:
        settings (ApplicationSettings): The settings object containing application settings.
        window (tk.Toplevel): The main settings window.
        main_frame (tk.Frame): The main frame containing the notebook.
        notebook (ttk.Notebook): The notebook widget containing different settings tabs.
        basic_frame (ttk.Frame): The frame for basic settings.
        advanced_frame (ttk.Frame): The frame for advanced settings.
        docker_settings_frame (ttk.Frame): The frame for Docker settings.
        basic_settings_frame (tk.Frame): The scrollable frame for basic settings.
        advanced_settings_frame (tk.Frame): The scrollable frame for advanced settings.
    """

    def __init__(self, settings, main_window):
        """
        Initializes the SettingsWindowUI.

        Args:
            settings (ApplicationSettings): The settings object containing application settings.
        """
        self.settings = settings
        self.main_window = main_window
        self.settings_window = None
        self.main_frame = None
        self.notebook = None
        self.basic_frame = None
        self.advanced_frame = None
        self.docker_settings_frame = None
        self.basic_settings_frame = None
        self.advanced_settings_frame = None
        

    def open_settings_window(self):
        """
        Opens the settings window.

        This method initializes and displays the settings window, including
        the notebook with tabs for basic, advanced, and Docker settings.
        """
        self.settings_window = tk.Toplevel()
        self.settings_window.title("Settings")
        self.settings_window.resizable(True, True)
        self.settings_window.grab_set()

        self.main_frame = tk.Frame(self.settings_window)
        self.main_frame.pack(expand=True, fill='both')

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(expand=True, fill='both')

        self.basic_frame = ttk.Frame(self.notebook)
        self.advanced_frame = ttk.Frame(self.notebook)
        self.docker_settings_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.basic_frame, text="Basic Settings")
        self.notebook.add(self.advanced_frame, text="Advanced Settings")
        self.notebook.add(self.docker_settings_frame, text="Docker Settings")

        self.basic_settings_frame = self.add_scrollbar_to_frame(self.basic_frame)
        self.advanced_settings_frame = self.add_scrollbar_to_frame(self.advanced_frame)

        self.create_basic_settings()
        self.create_advanced_settings()
        self.create_docker_settings()
        self.create_buttons()

    def add_scrollbar_to_frame(self, frame):
        """
        Adds a scrollbar to a given frame.

        Args:
            frame (tk.Frame): The frame to which the scrollbar will be added.

        Returns:
            tk.Frame: The scrollable frame.
        """
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    def create_basic_settings(self):
        """
        Creates the basic settings UI elements.

        This method creates and places UI elements for basic settings such as
        KOBOLDCPP IP, WHISPERAUDIO IP, OpenAI API Key, and SSL settings.
        """

        row_idx = 0

        tk.Label(self.basic_settings_frame, text="KOBOLDCPP IP:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        self.koboldcpp_ip_entry = tk.Entry(self.basic_settings_frame, width=25)
        self.koboldcpp_ip_entry.insert(0, self.settings.KOBOLDCPP_IP)
        self.koboldcpp_ip_entry.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        tk.Label(self.basic_settings_frame, text="PORT:").grid(row=row_idx, column=2, padx=0, pady=5, sticky="w")
        self.koboldcpp_port_entry = tk.Entry(self.basic_settings_frame, width=10)
        self.koboldcpp_port_entry.insert(0, self.settings.KOBOLDCPP_PORT)
        self.koboldcpp_port_entry.grid(row=row_idx, column=3, padx=0, pady=5, sticky="w")

        row_idx += 1

        tk.Label(self.basic_settings_frame, text="WHISPERAUDIO IP:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        self.whisperaudio_ip_entry = tk.Entry(self.basic_settings_frame, width=25)
        self.whisperaudio_ip_entry.insert(0, self.settings.WHISPERAUDIO_IP)
        self.whisperaudio_ip_entry.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        tk.Label(self.basic_settings_frame, text="PORT:").grid(row=row_idx, column=2, padx=0, pady=5, sticky="w")
        self.whisperaudio_port_entry = tk.Entry(self.basic_settings_frame, width=10)
        self.whisperaudio_port_entry.insert(0, self.settings.WHISPERAUDIO_PORT)
        self.whisperaudio_port_entry.grid(row=row_idx, column=3, padx=0, pady=5, sticky="w")

        row_idx += 1

        tk.Label(self.basic_settings_frame, text="OpenAI API Key:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        self.openai_api_key_entry = tk.Entry(self.basic_settings_frame, width=25)
        self.openai_api_key_entry.insert(0, self.settings.OPENAI_API_KEY)
        self.openai_api_key_entry.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        row_idx += 1

        tk.Label(self.basic_settings_frame, text="API Style:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        api_options = ["OpenAI"]
        self.api_dropdown = ttk.Combobox(self.basic_settings_frame, values=api_options, width=15, state="readonly")
        self.api_dropdown.current(api_options.index(self.settings.API_STYLE))
        self.api_dropdown.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        row_idx += 1

        self.ssl_enable_var = tk.IntVar(value=int(self.settings.SSL_ENABLE))
        tk.Label(self.basic_settings_frame, text="Enable SSL:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        self.ssl_enable_checkbox = tk.Checkbutton(self.basic_settings_frame, variable=self.ssl_enable_var)
        self.ssl_enable_checkbox.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        row_idx += 1

        self.ssl_selfcert_var = tk.IntVar(value=int(self.settings.SSL_SELFCERT))
        tk.Label(self.basic_settings_frame, text="Self-Signed Cert:").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        self.ssl_selfcert_checkbox = tk.Checkbutton(self.basic_settings_frame, variable=self.ssl_selfcert_var)
        self.ssl_selfcert_checkbox.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")

        row_idx += 1

        tk.Label(self.basic_settings_frame, text="Models").grid(row=row_idx, column=0, padx=0, pady=5, sticky="w")
        models_drop_down_options = self.settings.get_available_models() or ["No models available"]

        self.models_drop_down = ttk.Combobox(self.basic_settings_frame, values=models_drop_down_options, width=15, state="readonly")
        self.models_drop_down.current(api_options.index(self.settings.API_STYLE))
        self.models_drop_down.grid(row=row_idx, column=1, padx=0, pady=5, sticky="w")
        
        refresh_button = ttk.Button(self.basic_settings_frame, text="↻", command=lambda: (self.save_settings(False), self.settings.update_models_dropdown(self.models_drop_down)), width=4)
        refresh_button.grid(row=row_idx, column=2, columnspan=1, padx=0, pady=5, sticky="w")
        tt.Tooltip(refresh_button, text="Refresh the list of available models")

        row_idx += 1

        self.create_editable_settings(self.basic_settings_frame, self.settings.basic_settings, start_row=row_idx)

    def create_advanced_settings(self):
        """
        Creates the advanced settings UI elements.

        This method creates and places UI elements for advanced settings such as
        editable settings, pre-prompting, and post-prompting text areas.
        """
        self.create_editable_settings(self.advanced_settings_frame, self.settings.advanced_settings)

        tk.Label(self.advanced_settings_frame, text="Pre Prompting").grid(row=len(self.settings.advanced_settings), column=0, padx=0, pady=5, sticky="w")
        self.aiscribe_text = tk.Text(self.advanced_settings_frame, height=10, width=25)
        self.aiscribe_text.insert(tk.END, self.settings.AISCRIBE)
        self.aiscribe_text.grid(row=len(self.settings.advanced_settings), column=1, columnspan=2, padx=0, pady=5, sticky="w")

        tk.Label(self.advanced_settings_frame, text="Post Prompting").grid(row=len(self.settings.advanced_settings)+1, column=0, padx=0, pady=5, sticky="w")
        self.aiscribe2_text = tk.Text(self.advanced_settings_frame, height=10, width=25)
        self.aiscribe2_text.insert(tk.END, self.settings.AISCRIBE2)
        self.aiscribe2_text.grid(row=len(self.settings.advanced_settings)+1, column=1, columnspan=2, padx=0, pady=5, sticky="w")

    def create_docker_settings(self):
        """
        Creates the Docker settings UI elements.

        This method creates and places UI elements for Docker settings.
        """
        self.create_editable_settings(self.docker_settings_frame, self.settings.docker_settings)

    def create_editable_settings(self, frame, settings_set, start_row=0):
        """
        Creates editable settings UI elements.

        Args:
            frame (tk.Frame): The frame in which to create the settings.
            settings_set (list): The list of settings to create UI elements for.
            start_row (int): The starting row for placing the settings.
        """
        for i, setting in enumerate(settings_set):
            tk.Label(frame, text=f"{setting}:").grid(row=start_row+i, column=0, padx=0, pady=5, sticky="w")
            
            value = self.settings.editable_settings[setting]
            if value in [True, False]:
                var = tk.IntVar(value=int(value))
                checkbox = tk.Checkbutton(frame, variable=var)
                checkbox.grid(row=start_row+i, column=1, padx=0, pady=5, sticky="w")
                self.settings.editable_settings_entries[setting] = var
            else:
                entry = tk.Entry(frame)
                entry.insert(0, str(value))
                entry.grid(row=start_row+i, column=1, padx=0, pady=5, sticky="w")
                self.settings.editable_settings_entries[setting] = entry

    def create_buttons(self):
        """
        Creates the buttons for the settings window.

        This method creates and places buttons for saving settings, resetting to default,
        and closing the settings window.
        """
        tk.Button(self.main_frame, text="Save", command=self.save_settings, width=10).pack(side="right", padx=2, pady=5)
        tk.Button(self.main_frame, text="Default", width=10, command=self.reset_to_default).pack(side="right", padx=2, pady=5)
        tk.Button(self.main_frame, text="Close", width=10, command=self.settings_window.destroy).pack(side="right", padx=2, pady=5)

    def save_settings(self, close_window=True):
        """
        Saves the settings entered by the user.

        This method retrieves the values from the UI elements and calls the
        `save_settings` method of the `settings` object to save the settings.
        """
        self.settings.save_settings(
            self.koboldcpp_ip_entry.get(),
            self.whisperaudio_ip_entry.get(),
            self.openai_api_key_entry.get(),
            self.aiscribe_text.get("1.0", tk.END),
            self.aiscribe2_text.get("1.0", tk.END),
            self.settings_window,
            self.koboldcpp_port_entry.get(),
            self.whisperaudio_port_entry.get(),
            self.ssl_enable_var.get(),
            self.ssl_selfcert_var.get(),
            self.api_dropdown.get(),

        )

        if self.settings.editable_settings["Use Docker Status Bar"] and self.main_window.docker_status_bar is None:
            self.main_window.create_docker_status_bar()
        elif not self.settings.editable_settings["Use Docker Status Bar"] and self.main_window.docker_status_bar is not None:
            self.main_window.destroy_docker_status_bar()

        if close_window:
            self.settings_window.destroy()

    def reset_to_default(self):
        """
        Resets the settings to their default values.

        This method calls the `clear_settings_file` method of the `settings` object
        to reset the settings to their default values.
        """
        self.settings.clear_settings_file(self.settings_window)