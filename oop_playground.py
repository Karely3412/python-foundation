class MakeUp:
    make_up = {}

    def __init__(self, diff_foundation, diff_eye_shadow, diff_eye_liner, diff_lip_stick, diff_blush):
        self.foundation = diff_foundation
        self.eye_shadow = diff_eye_shadow
        self.eye_liner = diff_eye_liner
        self.lip_stick = diff_lip_stick
        self.blush = diff_blush

    
    def variety_makeup(self, diff_foundation):
        self.foundation = diff_foundation
        return f"New foundation color {self.foundation} added"
    





