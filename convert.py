import json
import sys
import glob

def convert(js_file):
    try:
        with open(js_file, 'r', encoding='utf-8') as f:
            dom = json.load(f)
            
        cfg = {}
        cfg['fov'] = dom['CameraFOV']
        cfg['x'] = dom['FreeCameraTransform']['localPosition']['x']
        cfg['y'] = dom['FreeCameraTransform']['localPosition']['y']
        cfg['z'] = dom['FreeCameraTransform']['localPosition']['z']
        cfg['rx'] = dom['FreeCameraTransform']['localRotation']['eulerAngles']['x']
        cfg['ry'] = dom['FreeCameraTransform']['localRotation']['eulerAngles']['y']
        cfg['rz'] = dom['FreeCameraTransform']['localRotation']['eulerAngles']['z']
        
        with open(js_file + '.cfg', 'w') as w:
            for key in cfg:
                w.write(f"{key}={cfg[key]:.10f}\n")
    except FileNotFoundError:
        print("Cannot find file " + js_file)
        
    
if __name__ == '__main__':

    if len(sys.argv) != 2:
        # print("Usage: python3 convert.py [VMC_Config_File.json]")
        for js in glob.glob('./*.json'):
            print(f"Convert {js}")
            convert(js)
    else:
        convert(sys.argv[1])
