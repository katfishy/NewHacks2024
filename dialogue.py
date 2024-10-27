# dialogue.py
class Dialogue:
    def __init__(self, dialogues):
        self.dialogues = dialogues
        self.current_dialogue_index = 0
        self.finished = False

    def get_current_dialogue(self):
        # 返回当前对话内容
        if self.current_dialogue_index < len(self.dialogues):
            return self.dialogues[self.current_dialogue_index]
        else:
            self.finished = True
            return None

    def next_dialogue(self):
        # 跳到下一个对话
        self.current_dialogue_index += 1
        if self.current_dialogue_index >= len(self.dialogues):
            self.finished = True

    def is_finished(self):
        # 检查对话是否结束
        return self.finished
