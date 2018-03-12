import ctypes

DLL_PATH = 'C:/tesseract/build/bin/Release/tesseract305.dll'
TESSDATA_PREFIX = b'./tessdata'
lang = b'eng'

tesseract = ctypes.cdll.LoadLibrary(DLL_PATH)
tesseract.TessBaseAPICreate.restype = ctypes.c_uint64
api = tesseract.TessBaseAPICreate()
rc = tesseract.TessBaseAPIInit3(ctypes.c_uint64(api), TESSDATA_PREFIX, lang)
if rc:
    tesseract.TessBaseAPIDelete(ctypes.c_uint64(api))
    print('Could not initialize tesseract.\n')
    exit(3)


def from_file(path):
    tesseract.TessBaseAPIProcessPages(
        ctypes.c_uint64(api), path, None, 0, None)
    tesseract.TessBaseAPIGetUTF8Text.restype = ctypes.c_uint64
    text_out = tesseract.TessBaseAPIGetUTF8Text(ctypes.c_uint64(api))
    return ctypes.string_at(text_out)


if __name__ == '__main__':
    image_file_path = b'./phototest.tif'
    result = from_file(image_file_path)
    print(result)
