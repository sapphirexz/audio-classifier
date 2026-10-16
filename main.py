from config import FLOW_DATA

class AudioFlowClassifier:
    def __init__(self):
        # 直接使用导入的 FLOW_DATA
        self.flow = FLOW_DATA

    def get_input(self, hint_type="yes_no"):
        while True:
            user_input = input("> ").strip().lower()
            if user_input in ["yes", "y"]:
                return True
            elif user_input in ["no", "n"]:
                return False
            else:
                print("Invalid input, please follow the prompt, e.g., Yes / No")

    def run(self):
        current = "node1"
        while True:
            if current.startswith("result_"):
                result = current.replace("result_", "")
                print("\n===============================")
                print(f"Final Classification Result: {result}")
                print("===============================")
                break
            node = self.flow[current]
            print("\n===============================")
            print(node["title"])
            print(f"Question: {node['question']}")
            print(f"Description: {node['desc']}")
            print(node["input_hint"])
            answer = self.get_input()
            current = node["yes"] if answer else node["no"]

if __name__ == "__main__":
    app = AudioFlowClassifier()
    app.run()