# Html template comiple to html files using jinja2 engine for Sublime Text3
# author: yswang(wangys0927@gmail.com)
# version: 0.1.0-2015/02/04

import os
import sys
import re
import codecs
import functools
import sublime
import sublime_plugin

from jinja2 import Template 
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

package_name='Htmlc'

CFG_TEMPLATE_DIR='template_dir'
CFG_OUTPUT_DIR='output_dir'
CFG_AUTO_COMPILE='auto_compile'
CFG_ENCODING='encoding'
DEF_ENCODING='UTF-8'


#get htmlc setting
def getSetting():
  # default settings
  config = sublime.load_settings('htmlc.sublime-settings')
  # load project htmlc settings
  project_config = sublime.active_window().active_view().settings().get("htmlc")
  if project_config is None:
    project_config = {}

  return {
    'template_dir': normalizePath(project_config.get(CFG_TEMPLATE_DIR, config.get(CFG_TEMPLATE_DIR, ''))),
    'output_dir': normalizePath(project_config.get(CFG_OUTPUT_DIR, config.get(CFG_OUTPUT_DIR, ''))),
    'auto_compile': project_config.get(CFG_AUTO_COMPILE, config.get(CFG_AUTO_COMPILE, True)),
    'encoding': project_config.get(CFG_ENCODING, config.get(CFG_ENCODING, DEF_ENCODING))
  }


# compile all htmlc files in current template dir 
def htmlcAll():
  cfg = getSetting()
  _tmpl_dir = cfg[CFG_TEMPLATE_DIR]
  if (os.path.exists(_tmpl_dir)==False):
    return
  # list all htmlc files
  for root, dirs, files in os.walk(_tmpl_dir):
    for filepath in files:
      htmlc(os.path.join(root, filepath))


# compile single htmlc file
def htmlc(filepath):
  if filepath is None:
    return

  (fileroot, fileext) = os.path.splitext(filepath)
  if (fileext != '.htmlc'):
    return

  cfg = getSetting()
  _tmpl_dir = cfg[CFG_TEMPLATE_DIR]
  _output_dir = cfg[CFG_OUTPUT_DIR]
  _encoding = cfg[CFG_ENCODING]

  (tmpl_file_dir, tmpl_file_name)=os.path.split(filepath);

  if _tmpl_dir=='':
    _tmpl_dir=tmpl_file_dir

  if _output_dir=='':
    _output_dir=tmpl_file_dir

  # relative path from current file path
  if (_output_dir.startswith('./') or _output_dir.startswith('../') or _output_dir.startswith('.\\') or _output_dir.startswith('..\\')):
    _output_dir=os.path.join(tmpl_file_dir, _output_dir)

  # parse relative path: ./ ../ if exists
  _output_dir=os.path.normpath(_output_dir)

  if os.path.exists(_tmpl_dir)==False:
    sublime.error_message('The template dir "'+ _tmpl_dir +'" is not exists!')

  if os.path.exists(_output_dir)==False:
    os.makedirs(_output_dir)

  try:
    templateLoader=FileSystemLoader(_tmpl_dir, encoding=_encoding)
    templateEnv=Environment(loader=templateLoader, 
        block_start_string='{%', block_end_string='%}', 
        variable_start_string='{{', variable_end_string='}}', 
        comment_start_string='{#', comment_end_string='#}', 
        trim_blocks=False, optimized=True, auto_reload=True, autoescape=False, cache_size=0)

  except Exception as ex:
    sublime.error_message('Error: Failed to init jinja2 Environment: {0} !'.format(str(ex)))


  tmpl_file_subdir=''
  if tmpl_file_dir.startswith(_tmpl_dir):
    # delete the template dir prevfix path
    tmpl_file_subdir=tmpl_file_dir[len(_tmpl_dir)+1:]

  
  status_msg=''
  # get template file
  try:
    template = templateEnv.get_template(os.path.join(tmpl_file_subdir, tmpl_file_name).replace(os.sep, '/'))
    _html = template.render()

    # make the absolute output dirs if not exists
    output_abpath=os.path.join(_output_dir, tmpl_file_subdir)
    if os.path.exists(output_abpath)==False:
      os.makedirs(output_abpath)

    (fname, fext)=os.path.splitext(tmpl_file_name)

    output_file=os.path.join(output_abpath, fname+'.html')
    
    html_file=codecs.open(output_file, 'w+', _encoding)
    html_file.write(_html)
    html_file.close()
    
    status_msg = 'O(∩_∩)O Comiple ['+ tmpl_file_name +'] to ['+ output_file +'] success!! O(∩_∩)O~'

  except TemplateNotFound as ex:
    err_msg = bytes(str(ex), encoding = 'utf-8')
    status_msg="Error: Template {0} not found!".format(str(err_msg, encoding = 'utf-8'))
    sublime.error_message(status_msg)
  except Exception as e:
    err_msg = bytes(str(e), encoding = 'utf-8')
    status_msg="Error: Failed to output html file: {0} !".format(str(err_msg, encoding = 'utf-8'))
    sublime.error_message(status_msg)

  sublime.set_timeout(functools.partial(status, status_msg), 1200);
  sublime.set_timeout(functools.partial(reloadHtml, output_file), 400);


def normalizePath(path):
  if (path.endswith(os.sep)):
    path=path[:-1]
  return path

def status(msg):
  sublime.status_message(msg)

#reload the opened html file
def reloadHtml(htmlfile):
  cfg=getSetting()
  for win in sublime.windows():
    for view in win.views():
      if(view.file_name()==htmlfile):
        view.run_command("reopen", {"encoding": cfg[CFG_ENCODING]})


#Compile current htmlc file to html
class HtmlcToHtmlCommand(sublime_plugin.TextCommand):
  def run(self, text):
    filepath = self.view.file_name()
    if filepath is None:
      return
    htmlc(filepath)


#Compile all htmlc files to html in current project
class AllHtmlcToHtmlCommand(sublime_plugin.TextCommand):
  def run(self, text):
    htmlcAll()


#listener to save current htmlc file
class HtmlcToHtmlSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    cfg = getSetting()
    if cfg[CFG_AUTO_COMPILE]:
      view.run_command("htmlc_to_html")
