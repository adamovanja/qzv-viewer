import os
import warnings
import shutil
from IPython.display import display, IFrame, HTML
import zipfile
import click
import qiime2.sdk
from q2cli.core.config import CONFIG


def _extract_py_api(input_path, output_path='last_extract'):
    # adapted from
    # https://github.com/qiime2/q2cli/blob/master/q2cli/builtin/tools.py

    try:
        extracted_dir = qiime2.sdk.Result.extract(input_path, output_path)
    except (zipfile.BadZipFile, ValueError):
        raise click.BadParameter(
            '%s is not a valid QIIME 2 Result. Only QIIME 2 Artifacts and '
            'Visualizations can be extracted.' % input_path)
    else:
        success = 'Extracted %s to directory %s' % (input_path, extracted_dir)
        click.echo(CONFIG.cfg_style('success', success))

    return extracted_dir


def display_qzv(filepath_qzv):
    """
    Displays Q2 visualisers in Jupyter notebook

    Displays QIIME2 visualisers in `filepath_qzv` (file ending `.qzv`)
    in Jupyter Notebooks.

    Args:
        filepath_qzv (str): Path to qzv file to display

    Returns:
        IPython.lib.display.IFrame
    """
    # works for jupyter not for VScode
    extracted_dir = _extract_py_api(filepath_qzv, 'extract')
    path2data = os.path.join(extracted_dir, 'data')

    # display emperor if in data/ folder
    emperor_file = os.path.join(path2data, 'emperor.html')
    if os.path.isfile(emperor_file):
        path2html = emperor_file
    else:
        # display index
        path2html = os.path.join(path2data, 'index.html')

    return IFrame(path2html, width=950, height=600)


def clean_up(filenames):
    # required after display_qzv_vscode!
    # # backward os directory setting
    for file_name in filenames:
        try:
            os.remove(file_name)
        except:
            shutil.rmtree(file_name)


def display_qzv_vscode(filepath_qzv):
    """
    Displays Q2 visualisers in VSCode notebook

    Displays QIIME2 visualisers in `filepath_qzv` (file ending `.qzv`)
    in VScode notebook.

    Args:
        filepath_qzv (str): Path to qzv file to display

    Returns:
        List of filenames that were moved to project working directory
        that need to be deleted afterwards with `clean_up()`
    """

    extracted_dir = _extract_py_api(filepath_qzv, 'extract')
    path2data = os.path.join(extracted_dir, 'data')

    target_dir = os.getcwd()
    file_names = os.listdir(path2data)
    for file_name in file_names:
        shutil.move(os.path.join(path2data, file_name), target_dir)
    shutil.rmtree(extracted_dir)
    # todo: remove "extract" root
    # os.remove(extact_dir_name)
    # start_dir = os.getcwd()
    # os.chdir(path2data)

    # display emperor if in data/ folder
    emperor_file = 'emperor.html'
    if os.path.isfile(emperor_file):
        # path2html = emperor_file
        clean_up(file_names)
        raise ValueError("Emperor files can not be displayed in VSCode")
    else:
        # display index
        path2html = 'index.html'
        print(display(HTML(path2html)))
        warnings.warn(
            "To clean up working directory please run clean_up with returned"
            "filelist after this")

    return file_names
