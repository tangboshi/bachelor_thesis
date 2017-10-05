% This is the Department of Wireless Networks Diploma/M.Sc. Thesis Class
% BETA VERSION! (v. 2004-04-03)
% @edited version (v.2010-07-19)
% Questions?
% Please contact the author: Janne Riihij�rvi (jar@inets.rwth-aachen.de)
% Edited version to work with pdflatex by Dominik Zoeller (dzo@inets.rwth-aachen.de)

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{inets-thesis}[2015/03/27]

%\LoadClass[a4paper,11pt,twoside,openright]{memoir}
\LoadClass[a4paper,11pt,oneside, openright]{memoir}

\usepackage{palatino}
%\usepackage{eulervm}

% These packages were added by ORA
\usepackage{graphicx}
\usepackage{amsmath,amsthm,amsfonts,amssymb}
\usepackage{import}
\usepackage{algorithmicx}
\usepackage{algpseudocode}
\usepackage{graphicx}
\usepackage{amsmath,amsthm,amsfonts,amssymb}
\usepackage{textcomp}
\usepackage{acronym}
\usepackage[hyphens]{url}
\usepackage{units}
\usepackage[caption=false,font=footnotesize]{subfig}
\usepackage{longtable}
\usepackage{pdflscape}
\usepackage{framed}
\usepackage{courier}
\usepackage{cite}
\usepackage[latin1]{inputenc} 
\usepackage[T1]{fontenc}
\usepackage{threeparttable} % helpfull table extension
\usepackage{multirow} % tables with multiple rows
\usepackage{tabularx} % table with adjustable width
\usepackage{pdfpages} 
% ---
%include spacing environment
\DisemulatePackage{setspace}
\usepackage{setspace}

% avoid widows and clubs
\clubpenalty = 10000 
\widowpenalty = 10000 
\displaywidowpenalty = 10000

% avoid to much hyphenation
\hyphenpenalty=500 
\doublehyphendemerits=9000 
\finalhyphendemerits=6000

% remove PDF version warnings
\pdfminorversion=5

%
% Set up the page size (for A4)
%
\settrimmedsize{\stockheight}{\stockwidth}{*}
\settypeblocksize{22cm}{14.5cm}{*}
\setlrmargins{*}{*}{1}
\setulmargins{*}{*}{1.5}
\checkandfixthelayout

%
% Begin by creating the chapter heading style
%
\makechapterstyle{inets-dis}{%
  \renewcommand{\chapterheadstart}{\vspace*{20pt}}
  \renewcommand{\printchaptername}{}
  \renewcommand{\chapternamenum}{}
  \renewcommand{\printchapternum}{\centerline{\LARGE\scshape\thechapter}}
  \renewcommand{\afterchapternum}{\par\nobreak\vskip 15pt}
  \renewcommand{\printchaptertitle}[1]{%
  \begin{center}\LARGE\scshape{##1}\end{center}}
  \renewcommand{\afterchaptertitle}{\vskip20pt}
  \renewcommand{\chaptermark}[1]{\markleft{##1}}
}

%
% Activate the style
%
\chapterstyle{inets-dis}

%
% Do matching section and subsection heads
%
\renewcommand{\secheadstyle}{\large\scshape\raggedright}
\renewcommand{\subsecheadstyle}{\itshape\raggedright}
\renewcommand{\subsubsecheadstyle}{\itshape\raggedright}
\maxsecnumdepth{subsubsection}

%
% Caption style
% 

\captionnamefont{\scshape}

%
% Set up the headers and footers in a new pagestyle and activate it
%

\newcommand\nouppercase[1]{{%
       \let\uppercase\relax
       \let\MakeUppercase\relax
       \expandafter\let\csname MakeUppercase \endcsname\relax
       #1}}%

\copypagestyle{inets-dis}{headings}


\makeevenhead{inets-dis}{\nouppercase{\scshape\thepage}}{}%
                          {\nouppercase{\scshape\leftmark}}
\makeoddhead{inets-dis}{\nouppercase{\scshape\rightmark}}{}%
                          {\nouppercase{\scshape\thepage}}
\renewcommand{\chaptermark}[1]{\markboth{#1}{#1}}
\renewcommand{\sectionmark}[1]{\markright{#1}}
\makeatletter
\makepsmarks{inets-dis}{%
       \let\@mkboth\markboth
       \def\chaptermark##1{%
         \markboth{{%
           \ifnum \c@secnumdepth >\m@ne
             \if@mainmatter
               \thechapter. \ %
             \fi
           \fi
           ##1}}{}}%
      \def\tocmark{\markboth{\contentsname}{\contentsname}}
      %\def\lofmark{\markboth{\listfigurename}{\listfigurename}}
      %\def\lotmark{\markboth{\listtablename}{\listtablename}}
      \def\bibmark{\markboth{\bibname}{\bibname}}
      \def\indexmark{\markboth{\indexname}{\indexname}}
       \def\sectionmark##1{%
         \markright{{%
           \ifnum \c@secnumdepth > \z@
             \thesection. \ %
           \fi
           ##1}}}%
     }
\makeatother
\pagestyle{inets-dis}

%
% Set up the Table of Contents
%
\maxtocdepth{subsection}

% Toc Xname fonts
\renewcommand{\cftchapterfont}{\large\scshape}
\renewcommand{\cftsectionfont}{\scshape}
\renewcommand{\cftsubsectionfont}{\itshape}

% Toc Xpagenum fonts
\renewcommand{\cftchapterpagefont}{\large\scshape}
\renewcommand{\cftsectionfont}{\scshape}
\renewcommand{\cftsubsectionfont}{\scshape}

% Toc Xentry skips
\setlength{\cftbeforechapterskip}{12pt}
\setlength{\cftbeforesectionskip}{6pt}
\setlength{\cftbeforesubsectionskip}{0pt}


% We do not want skips between paragraphs
\setlength{\parskip}{0pt}


%
% Finally, some macros useful in the main exposition
%
\def\term#1{\textbf{#1}}
\newcommand{\mterm}[2][]{%
  \def\temp{#1}%
  \term{#2}%
  \ifx\temp\empty
    \marginpar{\small\itshape #2}
  \else
    \marginpar{\small\itshape #1}
  \fi
}

\newcommand{\ThesisTitle}[1]{\newcommand{\thesistitle}{#1}}

\newcommand{\ThesisDate}[3]{\newcounter{thesisday}
\setcounter{thesisday}{#3}\newcommand{\thesisdate}{%
\ifnum#2=1January\fi\ifnum#2=2February\fi\ifnum#2=3March\fi
\ifnum#2=4April\fi\ifnum#2=5May\fi\ifnum#2=6June\fi
\ifnum#2=7July\fi\ifnum#2=8August\fi\ifnum#2=9September\fi
\ifnum#2=10October\fi\ifnum#2=11November\fi\ifnum#2=12December\fi
~\arabic{thesisday},~#1}}

\newcommand{\thesistype}{(!)}
\newcommand{\ThesisType}[1]{%
\ifx#1M\renewcommand{\thesistype}{Master~Thesis}\fi
\ifx#1B\renewcommand{\thesistype}{Bachelor~Thesis}\fi}

\newcommand{\ThesisAuthor}[1]{\newcommand{\thesisauthor}{#1}}
\newcommand{\FirstExaminerName}[1]{\newcommand{\firstexaminername}{#1}}
\newcommand{\SecondExaminerName}[1]{\newcommand{\secondexaminername}{#1}}
\newcommand{\SupervisorNames}[1]{\newcommand{\supervisornames}{#1}}

\usepackage[pdffitwindow=true,pdfduplex=DuplexFlipLongEdge,pdfdisplaydoctitle=true,pdfpagelabels=true,hyperindex=true,hyperfootnotes=true,hyperfigures=true,bookmarks=true]{hyperref}
\usepackage[all]{hypcap}

\AtBeginDocument{%
\hypersetup{
	pdftitle={\thesistitle},
	pdfauthor={\thesisauthor},
	pdfsubject={\thesistype, Institute for Networked Systems, RWTH Aachen University},
	bookmarksnumbered=true,
	bookmarksopen=true,
	bookmarksopenlevel=1,
	pdfborder={0 0 0},
	plainpages=false,
	pdfcreator={\thesisauthor},
}
\frontmatter
\setcounter{page}{0} %workaround to resolve PDF page reference problem.
\title{
    {  
        \LARGE\thesistitle
    }
}
\author{\LARGE\thesisauthor}
\date{
    \vspace{10mm}
    {\large \thesistype} \\
    \vspace{3mm}
    {\large \thesisdate}
    \vfill
    \large \textbf{Examiners} \\
   \vspace{2mm}\firstexaminername \\ \secondexaminername \\\vspace{5mm}\large \textbf{Supervisors}\vspace{2mm} \\ \firstexaminername \\ \supervisornames \\
    \vspace{15mm}
    {\Large Institute for Networked Systems} \\
    \vspace{1mm}
    {\Large RWTH Aachen University} \\
    \vspace{15mm}}

\maketitle
    \hbox to \textwidth{%
        \hfill\includegraphics[width=0.7\textwidth]{pictures/inets_new}\hfill
    }
\cleardoublepage
\noindent\textsf{\textbf{The present work was submitted to the Institute for Networked Systems}\\
\vspace{25mm}\\
\thesistitle\\
\vspace{15mm}\\
\thesistype\\
\vspace{35mm}\\
presented by\\
\thesisauthor\\
\vspace{35mm}\\
\firstexaminername \\
\secondexaminername\\
\vspace{20mm}\\
Aachen, \thesisdate\\
\vspace{5mm}\\
\line(1,0){180}\\
\footnotesize{(\thesisauthor)} }
% free pages after title
\thispagestyle{empty}   
\pagenumbering{Roman}
\cleardoublepage
\chapter{Acknowledgements}
\input{acknowledgements}
\cleardoublepage
\tableofcontents
\cleardoublepage
\chapter{Abstract}
\input{abstract}
\cleardoublepage
\mainmatter}

\AtEndDocument{
\addtocontents{lof}{\par}
\addtocontents{lot}{\par}
\backmatter
%\listoftables\newpage
%\listoffigures
\begin{spacing}{1.0}
    \bibliography{IEEEfull,bibliography}
    \bibliographystyle{IEEE}   
\end{spacing}
% \bibliographystyle{alpha}

\addcontentsline{toc}{chapter}{Declaration}
\includepdf[pages={1}]{appendices/Formular_Eidesstattliche_Versicherung_neu.pdf}

}
\AtEndOfClass{\input{owndefs}}

% ---end of addition by ORA---
