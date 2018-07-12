import TinMan
from TinMan import AgentHost
from TinMan_Samples.WavingAgent import WavingAgent

if __name__ == "__main__":
    print('''
    Sample Agent Launcher
    ---------------------------
    Choose one of the following:
    
    1 WavingAgent
    2 HingeCharacterisationAgent
    3 FullHouse
    4 InteractiveAgent
    5 MinimalAgent
    6 SoccerbotAgent
    7 RoboVizDemoAgent
    8 Social Agent
    9 PidAgent
    0 WizardExample
    S DebugShapeTransformationAgent
    ''')
    inp = input("Enter key")
    if inp == '1':
        AgentHost.AgentHost().run(WavingAgent())