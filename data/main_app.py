import tkinter as tk
from tkinter import messagebox, simpledialog
from pathlib import Path
import plistlib
import traceback
from exploit.restore import restore_file

class MobileGestaltApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nugget GUI by LeminLimez (GUI : everxqzw)")
        
        self.running = True
        self.passed_check = False
        self.dynamic_island_enabled = False
        self.current_model_name = ""
        self.boot_chime_enabled = False
        self.charge_limit_enabled = False
        self.stage_manager_enabled = False
        self.shutter_sound_enabled = False
        self.always_on_display_enabled = False
        self.apple_pencil_enabled = False
        self.action_button_enabled = False
        self.internal_storage_enabled = False
        self.gestalt_path = Path.joinpath(Path.cwd(), "com.apple.MobileGestalt.plist")
        
        self.create_widgets()
        self.check_file()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, height=20, width=80)
        self.text_area.pack()
        self.text_area.insert(tk.END, "by LeminLimez\nv1.2\n\n")
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        
        self.dynamic_island_button = tk.Button(self.buttons_frame, text="Toggle Dynamic Island", command=self.toggle_dynamic_island)
        self.dynamic_island_button.pack(fill=tk.X)
        
        self.set_model_name_button = tk.Button(self.buttons_frame, text="Set Device Model Name", command=self.set_model_name)
        self.set_model_name_button.pack(fill=tk.X)
        
        self.boot_chime_button = tk.Button(self.buttons_frame, text="Toggle Boot Chime", command=self.toggle_boot_chime)
        self.boot_chime_button.pack(fill=tk.X)
        
        self.charge_limit_button = tk.Button(self.buttons_frame, text="Toggle Charge Limit", command=self.toggle_charge_limit)
        self.charge_limit_button.pack(fill=tk.X)
        
        self.stage_manager_button = tk.Button(self.buttons_frame, text="Toggle Stage Manager Supported", command=self.toggle_stage_manager)
        self.stage_manager_button.pack(fill=tk.X)
        
        self.shutter_sound_button = tk.Button(self.buttons_frame, text="Disable Region Restrictions", command=self.toggle_shutter_sound)
        self.shutter_sound_button.pack(fill=tk.X)
        
        self.always_on_display_button = tk.Button(self.buttons_frame, text="Always On Display", command=self.toggle_always_on_display)
        self.always_on_display_button.pack(fill=tk.X)
        
        self.apple_pencil_button = tk.Button(self.buttons_frame, text="Toggle Apple Pencil", command=self.toggle_apple_pencil)
        self.apple_pencil_button.pack(fill=tk.X)
        
        self.action_button = tk.Button(self.buttons_frame, text="Toggle Action Button", command=self.toggle_action_button)
        self.action_button.pack(fill=tk.X)
        
        self.internal_storage_button = tk.Button(self.buttons_frame, text="Toggle Internal Storage", command=self.toggle_internal_storage)
        self.internal_storage_button.pack(fill=tk.X)
        
        self.apply_button = tk.Button(self.buttons_frame, text="Apply", command=self.apply_changes)
        self.apply_button.pack(fill=tk.X)
        
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=self.exit_program)
        self.exit_button.pack(fill=tk.X)
    
    def check_file(self):
        if Path.exists(self.gestalt_path) and Path.is_file(self.gestalt_path):
            self.passed_check = True
            self.update_text_area("MobileGestalt : OK")

        else:
            self.passed_check = False
            self.update_text_area("No MobileGestalt file found!\nPlease place the file in the correct directory.")
            choice = messagebox.askquestion("File Not Found", "No MobileGestalt file found. Retry or enter path?", icon='warning')
            if choice == 'yes':
                self.gestalt_path = Path("com.apple.MobileGestalt.plist")
            else:
                new_path = simpledialog.askstring("Enter Path", "Enter new path to file:")
                self.gestalt_path = Path(new_path)
                self.check_file()
    
    def update_text_area(self, message):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, message)
    
    def toggle_dynamic_island(self):
        self.dynamic_island_enabled = not self.dynamic_island_enabled
        self.update_text_area(f"Dynamic Island Enabled: {self.dynamic_island_enabled}")
    
    def set_model_name(self):
        name = simpledialog.askstring("Set Model Name", "Enter Model Name (Leave blank to turn off custom name):")
        self.current_model_name = name or ""
        self.update_text_area(f"Model Name Set: {self.current_model_name}")

    def toggle_boot_chime(self):
        self.boot_chime_enabled = not self.boot_chime_enabled
        self.update_text_area(f"Boot Chime Enabled: {self.boot_chime_enabled}")

    def toggle_charge_limit(self):
        self.charge_limit_enabled = not self.charge_limit_enabled
        self.update_text_area(f"Charge Limit Enabled: {self.charge_limit_enabled}")

    def toggle_stage_manager(self):
        self.stage_manager_enabled = not self.stage_manager_enabled
        self.update_text_area(f"Stage Manager Enabled: {self.stage_manager_enabled}")

    def toggle_shutter_sound(self):
        self.shutter_sound_enabled = not self.shutter_sound_enabled
        self.update_text_area(f"Shutter Sound Enabled: {self.shutter_sound_enabled}")

    def toggle_always_on_display(self):
        self.always_on_display_enabled = not self.always_on_display_enabled
        self.update_text_area(f"Always On Display Enabled: {self.always_on_display_enabled}")

    def toggle_apple_pencil(self):
        self.apple_pencil_enabled = not self.apple_pencil_enabled
        self.update_text_area(f"Apple Pencil Enabled: {self.apple_pencil_enabled}")

    def toggle_action_button(self):
        self.action_button_enabled = not self.action_button_enabled
        self.update_text_area(f"Action Button Enabled: {self.action_button_enabled}")

    def toggle_internal_storage(self):
        self.internal_storage_enabled = not self.internal_storage_enabled
        self.update_text_area(f"Internal Storage Enabled: {self.internal_storage_enabled}")

    def apply_changes(self):
        if not self.passed_check:
            messagebox.showerror("Error", "No valid MobileGestalt file found!")
            return
        
        try:
            with open(self.gestalt_path, 'rb') as in_fp:
                plist = plistlib.load(in_fp)
            
            if self.dynamic_island_enabled:
                plist["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["ArtworkDeviceSubType"] = 2556
            if self.current_model_name:
                plist["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["ArtworkDeviceProductDescription"] = self.current_model_name
            if self.boot_chime_enabled:
                plist["CacheExtra"]["QHxt+hGLaBPbQJbXiUJX3w"] = True
            if self.charge_limit_enabled:
                plist["CacheExtra"]["37NVydb//GP/GrhuTN+exg"] = True
            if self.stage_manager_enabled:
                plist["CacheExtra"]["qeaj75wk3HF4DwQ8qbIi7g"] = 1
            if self.shutter_sound_enabled:
                plist["CacheExtra"]["h63QSdBCiT/z0WU6rdQv6Q"] = "US"
                plist["CacheExtra"]["zHeENZu+wbg7PUprwNwBWg"] = "LL/A"
            if self.always_on_display_enabled:
                plist["CacheExtra"]["2OOJf1VhaM7NxfRok3HbWQ"] = True
                plist["CacheExtra"]["j8/Omm6s1lsmTDFsXjsBfA"] = True
            if self.apple_pencil_enabled:
                plist["CacheExtra"]["yhHcB0iH0d1XzPO/CFd3ow"] = True
            if self.action_button_enabled:
                plist["CacheExtra"]["cT44WE1EohiwRzhsZ8xEsw"] = True
            if self.internal_storage_enabled:
                plist["CacheExtra"]["LBJfwOEzExRxzlAnSuI7eg"] = True

            with open(self.gestalt_path, 'wb') as out_fp:
                plistlib.dump(plist, out_fp)
            
            restore_file(fp=self.gestalt_path, restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/", restore_name="com.apple.MobileGestalt.plist")
            messagebox.showinfo("Success", "Changes applied! Reboot your device to see the changes.")
        
        except Exception as e:
            self.update_text_area(traceback.format_exc())
            messagebox.showerror("Error", f"An error occurred: {e}")

    def exit_program(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MobileGestaltApp(root)
    root.mainloop()
