import numpy as np
import pydicom


def read_and_sort_dicom_files(dcm_files, return_dcm_files=False):
    # list, read, sort dicom files
    dcm_handlers = [pydicom.read_file(item, force=True) for item in dcm_files]

    # sort in ascending order
    z_positions = []
    for dcm_handler in dcm_handlers:
        x = dcm_handler.ImageOrientationPatient[0:3]
        y = dcm_handler.ImageOrientationPatient[3:6]
        z_dir = np.cross(x, y)
        z_positions.append(np.dot(z_dir, dcm_handler.ImagePositionPatient))
    sorted_dcm_handlers = [x for (y, x) in sorted(zip(z_positions, dcm_handlers))]
    sorted_dcm_files = [x for (y, x) in sorted(zip(z_positions, dcm_files))]

    if return_dcm_files:
        return sorted_dcm_files
    else:
        return sorted_dcm_handlers
