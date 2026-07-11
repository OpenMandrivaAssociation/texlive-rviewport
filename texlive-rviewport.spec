%global tl_name rviewport
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Relative Viewport for Graphics Inclusion
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rviewport
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Package graphicx provides a useful keyword viewport which allows to show
just a part of an image. However, one needs to put there the actual
coordinates of the viewport window. Sometimes it is useful to have
relative coordinates as fractions of natural size. For example, one may
want to print a large image on a spread, putting a half on a verso page,
and another half on the next recto page. For this one would need a
viewport occupying exactly one half of the file's bounding box, whatever
the actual width of the image may be. This package adds a new keyword
rviewport to the graphicx package specifying Relative Viewport for
graphics inclusion: a window defined by the given fractions of the
natural width and height of the image.

