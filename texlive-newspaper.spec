%global tl_name newspaper
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset newsletters to resemble newspapers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newspaper
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newspaper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The newspaper package redefines the page style and \maketitle command to
produce a typeset page similar to that of a newspaper. It also provides
several commands that (when used with other packages) simplify the
writing of articles in a newspaper-style column format.

