import webbrowser

c.Application.log_level = 30
c.NotebookApp.allow_remote_access = False
c.NotebookApp.allow_root = False
c.NotebookApp.base_url = '/'

webbrowser.register(
    'chrome',
    None,
    webbrowser.GenericBrowser(
        'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    )
)
c.NotebookApp.browser = 'chrome'
c.NotebookApp.webbrowser_open_new = 2

c.NotebookApp.default_url = '/tree'
c.NotebookApp.enable_mathjax = True
c.NotebookApp.extra_nbextensions_path = []
c.NotebookApp.extra_static_paths = []
c.NotebookApp.extra_template_paths = []
c.NotebookApp.ip = 'localhost'
c.NotebookApp.port = 8888
c.NotebookApp.jinja_environment_options = {}
c.NotebookApp.jinja_template_vars = {}
c.NotebookApp.max_buffer_size = 536870912
c.NotebookApp.nbserver_extensions = {}
c.NotebookApp.open_browser = True
c.NotebookApp.quit_button = True

#  Setting to an empty string disables authentication altogether, which is NOT
#  RECOMMENDED.
#c.NotebookApp.token = '<generated>'

c.NotebookApp.websocket_compression_options = None

c.MultiKernelManager.default_kernel_name = 'python3'
c.ContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo',
                                '.DS_Store', '*.so', '*.dylib', '*~', 'notebook_config.py']
c.ContentsManager.pre_save_hook = None
c.ContentsManager.untitled_directory = 'New Folder'
c.ContentsManager.untitled_file = 'untitled'
c.ContentsManager.untitled_notebook = 'New'
c.FileManagerMixin.use_atomic_writing = True
c.FileContentsManager.delete_to_trash = False
c.FileContentsManager.post_save_hook = None
