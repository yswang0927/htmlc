Htmlc(Html Compiler)
====================

# *Html template compile to html file for Sublime Text3* #

## **什么是 Htmlc** ##
Htmlc(Html Compiler)是一个在Sublime Text3下使用Python-jinja2模板引擎将编写的Html模板(使用jinja2的模板语法)编译为静态html文件的工具插件。

## **我什么会开发这个插件？** ##
因为 懒 ！<br>
诱因：<br>
    之前在开发一个互联网网站的静态html页面，该网站有几十个html页面，每个html页面都是四个部分组成（header/nav, side/menu, footer, main），其中 header/nav,side/menu,footer都是一样的，只有main块是变化的；我当时的做法是：先写好一个html页面，然后Ctrl+C/Ctrl+V下一个页面进行修改，就这样做下去。当全部做好给客户看时，客户说：在头部增加一个导航菜单项，在底部修改下Copyright等，然后我就开始把这几十个页面一个一个修改，直接把我搞的想吐！

    然后就想：如果这些静态的html页面能够支持动态的 include header,side,footer就好了，这样我就只需要修改一处，然后重新把这些html页面编译下，就生成了全新的html页面，该多爽啊！O(∩_∩)O

    想想自己在使用Java开发时一直都在用Apache Velocity模板引擎来生成页面，Velocity支持layout，很方便开发动态页面。但是，我总不能因为要编译输出静态Html页面，而使用Java开发一个应用程序吧，显然很不方便。

    同时，我又是使用Sublime Text来编写静态Html页面的，Sublime太强大和方便了，在有了开发前一个[Lessc for Sublime Text3](http://git.oschina.net/yswang/lessc) 插件的基础上，自然想到再开发一个插件来达到我通过模板编译输出Html的目的。

    于是Google Sublime的类似插件，我没有找到（如果谁有更好的，可以告诉我，哈哈） ，接着Google Python的web模板引擎，发现了很多，最终选择了[Jinja2](http://jinja.pocoo.org/)模板引擎；最终通过一天多的开发、测试和整理，我的 Htmlc(Html Compiler)插件就诞生了，其达到的效果完全满足了我目前的需求（说不定以后会有更高的要求呢O(∩_∩)O~）！！！

## **如何使用？** ##

- 1.下载所有代码(Htmlc、jinja2、markupsafe)-Htmlc依赖jinja2，jinja2需要markupsafe

- 2.将 `Htmlc` 文件夹扔到 `Sublime Text3安装目录\Data\Packages\` 下：

    `your sublime Text3\Data\Packages\Htmlc`

- 3.将 `jinja2` 和 `markupsafe` 文件夹扔到 `Sublime Text3的安装根目录下` ：

    `your sublime Text3\jinja2`
    `your sublime Text3\markupsafe`

    **说明：** Htmlc需要导入`jinja2`类库使用：`from jinja2 import *`，我在Sublime下测试了如何引入Python第三方库，发现只有将第三方库放到Sublime安装根目录下才能生效（我很想将jinja2和markupsafe放到我的Htmlc目录下，如果有谁知道可以放到插件目录下，很期待你告诉俺！）。

- 4.开始编写你的 `xx.htmlc` 文件(我定义了 `.htmlc` 扩展名，Htmlc只会编译此扩展名的文件)和 `layout` 文件，当你保存你的 `xx.htmlc`文件时，你就会惊讶的发现：Htmlc帮你编译输出了`xx.html`文件（包含了layout的布局文件内容）。

    **注意：** layout文件的扩展名随意(比如：.tmpl, .layout等)，但不能是`.htmlc`，因为layout文件仅仅是用来做layout布局的，不需要单独编译输出为独立的html文件。

- 5.Htmlc的模板语法请参考 `jinja2` 的语法说明，同时我也在Htmlc下添加了一个 `jinja2-docs.md`的中文翻译语法说明，可以在 `sublime text3\Preferences\Package Settings\Htmlc\Jinja2 Template Docs` 打开。


## **特性** ##
- Htmlc的默认设置和设置项可以从 `sublime text3\Preferences\Package Settings\Htmlc\Settings`看到和修改；

- Htmlc支持 **自动编译**（即时保存即时编译当前htmlc文件，由`auto_compile:true|false`决定）、 **手动编译** 和 **全部编译**；<br>
    手动编译 和 全部编译 可以通过配置快捷键（`sublime text3\Preferences\Package Settings\Htmlc\Key Bindings - Default`）进行，<br>也可以在工具命令：`sublime text3\Tools\Htmlc > html\Compile Current htmlc file | Compile All htmlc files` 下触发进行。

- Htmlc还支持 `.sublime-project` 项目私有化配置，这样可以为不同的项目进行不同的 Htmlc 的配置。<br>

`test.sublime-project` 示例配置：
>{<br>
>&nbsp;&nbsp;&nbsp;"folders":[<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name":&nbsp;"test",<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"path":"."<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
>&nbsp;&nbsp;&nbsp;],<br>
>&nbsp;&nbsp;&nbsp;"settings":<br>
>&nbsp;&nbsp;&nbsp;{<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"htmlc":<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"auto_compile":&nbsp;true,<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"encoding":&nbsp;"UTF-8",<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"output_dir":&nbsp;"D:\\workspace\\test\\build",<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"template_dir":&nbsp;"D:\\workspace\\test\\src\\htmlc"<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
>&nbsp;&nbsp;&nbsp;}<br>
>}

以上述`test.sublime-project`配置为例：<br>
项目test的htmlc模板目录在`D:\workspace\test\src\htmlc` 目录下，编译后的html文件输出在 `D:\workspace\test\build` 目录下。

##我的测试项目结构和配置
>test<br>
>└&nbsp;build<br>
>&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;css<br>
>&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;images<br>
>&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;js<br>
><br>
>└&nbsp;src<br>
>&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;htmlc<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;layout<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;default.layout<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;news<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;news.htmlc<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;china<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;china.htmlc<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;index.htmlc<br>
>
>└&nbsp;test.sublime-project<br>

当我对test项目进行htmlc全部编译后，在build下生成的目录结构如下：
>test<br>
>└&nbsp;build<br>
>&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;css<br>
>&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;images<br>
>&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;js<br>
>&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;news<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├&nbsp;news.html<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;china<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;china.html<br>
>&nbsp;&nbsp;&nbsp;&nbsp;└&nbsp;index.html<br>

### **附部分页面的代码** ###
**default.layout**
>&nbsp;&nbsp;&lt;!DOCTYPE&nbsp;html&gt;<br>
>&nbsp;&nbsp;&lt;html&gt;<br>
>&nbsp;&nbsp;&lt;head&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;meta&nbsp;charset="utf-8"&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;meta&nbsp;http-equiv="X-UA-Compatible"&nbsp;content="IE=edge,chrome=1"&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;title&gt;&nbsp;{%&nbsp;block&nbsp;title&nbsp;%}{%&nbsp;endblock&nbsp;%}&nbsp;-&nbsp;Htmlc&lt;/title&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;link&nbsp;rel="stylesheet"&nbsp;type="text/css"&nbsp;href="css/style.css"&gt;<br>
>&nbsp;&nbsp;&lt;/head&gt;<br>
>
>&nbsp;&nbsp;&lt;body&gt;<br>
>
>&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;header&nbsp;--&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;div&nbsp;id="header"&gt;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h2&gt;Header&lt;/h2&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;/div&gt;&nbsp;&lt;!--&nbsp;/end&nbsp;header&nbsp;--&gt;<br>
>
>&nbsp;&nbsp;&nbsp;&lt;div&nbsp;id="main-container"&gt;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{%&nbsp;block&nbsp;screen_body&nbsp;%}{%&nbsp;endblock&nbsp;%}<br>
>&nbsp;&nbsp;&nbsp;&lt;/div&gt;<br>
>
>&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;footer&nbsp;--&gt;<br>
>&nbsp;&nbsp;&nbsp;&lt;div&nbsp;id="footer"&gt;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copyright&nbsp;&copy;&nbsp;2015&nbsp;--&nbsp;yswang<br>
>&nbsp;&nbsp;&nbsp;&lt;/div&gt;&nbsp;&lt;!--&nbsp;/end&nbsp;footer&nbsp;--&gt;<br>
>
>&nbsp;&nbsp;&lt;/body&gt;<br>
>&nbsp;&nbsp;&lt;/html&gt;<br>

**index.htmlc**
>{%&nbsp;extends&nbsp;"layout/default.layout"&nbsp;%}<br>
>{%&nbsp;block&nbsp;title&nbsp;%}首页{%&nbsp;endblock&nbsp;%}&nbsp;<br>
>{%&nbsp;block&nbsp;screen_body&nbsp;%}<br>
>&lt;div&nbsp;class="w"&gt;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;哈哈，欢迎使用&nbsp;Htmlc&nbsp;for&nbsp;Sublime&nbsp;Text&nbsp;3&nbsp;to&nbsp;compile&nbsp;templates&nbsp;to&nbsp;html&nbsp;files&lt;/h1&gt;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&lt;h2&gt;作者：yswang&lt;/h2&gt;<br>
>&lt;/div&gt;<br>
>{%&nbsp;endblock&nbsp;%}<br>

**news.htmlc**
>{%&nbsp;extends&nbsp;"layout/default.layout"&nbsp;%}<br>
>{%&nbsp;block&nbsp;title&nbsp;%}新闻动态{%&nbsp;endblock&nbsp;%}<br>
>{%&nbsp;block&nbsp;screen_body&nbsp;%}<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;这里展示全球最新新闻动态&lt;/h1&gt;<br>
>{%&nbsp;endblock&nbsp;%}<br>

**china.htmlc**
>{%&nbsp;extends&nbsp;"layout/default.layout"&nbsp;%}<br>
>{%&nbsp;block&nbsp;title&nbsp;%}国内新闻动态{%&nbsp;endblock&nbsp;%}<br>
>{%&nbsp;block&nbsp;screen_body&nbsp;%}<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;这里展示中国的新闻动态&lt;/h1&gt;<br>
>{%&nbsp;endblock&nbsp;%}<br>

**编译后的 index.html**
>&lt;!DOCTYPE&nbsp;html&gt;<br>
>&lt;html&gt;<br>
>&lt;head&gt;<br>
>   &lt;meta&nbsp;charset="utf-8"&gt;<br>
>   &lt;meta&nbsp;http-equiv="X-UA-Compatible"&nbsp;content="IE=edge,chrome=1"&gt;<br>
>   &lt;title&gt;&nbsp;首页&nbsp;-&nbsp;Htmlc&lt;/title&gt;<br>
>   &lt;link&nbsp;rel="stylesheet"&nbsp;type="text/css"&nbsp;href="css/style.css"&gt;<br>
>&lt;/head&gt;<br>
>
>&lt;body&gt;<br>
>
>   &lt;!--&nbsp;header&nbsp;--&gt;<br>
>   &lt;div&nbsp;id="header"&gt;<br>
>       &lt;h2&gt;Header&lt;/h2&gt;<br>
>   &lt;/div&gt;&nbsp;&lt;!--&nbsp;/end&nbsp;header&nbsp;--&gt;<br>
>
>   &lt;div&nbsp;id="main-container"&gt;<br>
>       
>   &lt;div&nbsp;class="w"&gt;<br>
>       &lt;h1&gt;哈哈，欢迎使用&nbsp;Htmlc&nbsp;for&nbsp;Sublime&nbsp;Text&nbsp;3&nbsp;to&nbsp;compile&nbsp;templates&nbsp;to&nbsp;html&nbsp;files&lt;/h1&gt;<br>
>       &lt;h2&gt;作者：yswang&lt;/h2&gt;<br>
>   &lt;/div&gt;<br>
>
>   &lt;/div&gt;<br>
>   
>   &lt;!--&nbsp;footer&nbsp;--&gt;<br>
>   &lt;div&nbsp;id="footer"&gt;<br>
>       Copyright&nbsp;&copy;&nbsp;2015&nbsp;--&nbsp;yswang<br>
>   &lt;/div&gt;&nbsp;&lt;!--&nbsp;/end&nbsp;footer&nbsp;--&gt;<br>
>
>&lt;/body&gt;<br>
>&lt;/html&gt;<br>

##Thank you

