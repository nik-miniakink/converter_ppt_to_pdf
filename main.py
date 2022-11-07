import comtypes.client
import os

def print_hi(name):
    dir_name = os.getcwd()
    names = os.listdir(f'{dir_name}\\qwerty')
    for name in names:
        fullname = os.path.join(os.getcwd(), name)
        if os.path.isfile(fullname):
            print(fullname)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType=32):
    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName.replace(".pptx", "").replace(".ppt", "") + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType)  # formatType = 32 for ppt to pdf
    deck.Close()
    print('% s преобразование файла завершено' % outputFileName)


def convert_files_in_folder(powerpoint, folder):
    files = os.listdir(folder)
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    for pptfile in pptfiles:
        fullpath = os.path.join(cwd, pptfile)
        ppt_to_pdf(powerpoint, fullpath, fullpath)


if __name__ == "__main__":
    powerpoint = init_powerpoint()
    cwd = os.getcwd()
    convert_files_in_folder(powerpoint, cwd)
    powerpoint.Quit()