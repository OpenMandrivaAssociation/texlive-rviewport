# revision 23739
# category Package
# catalog-ctan /macros/latex/contrib/rviewport
# catalog-date 2011-08-28 17:37:31 +0200
# catalog-license lppl
# catalog-version v1.0
Name:		texlive-rviewport
Version:	v1.0
Release:	1
Summary:	Relative Viewport for Graphics Inclusion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rviewport
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rviewport.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package graphicx provides a useful keyword viewport which
allows to show just a part of an image. However, one needs to
put there the actual coordinates of the viewport window.
Sometimes it is useful to have relative coordinates as
fractions of natural size. For example, one may want to print a
large image on a spread, putting a half on a verso page, and
another half on the next recto page. For this one would need a
viewport occupying exactly one half of the file's bounding box,
whatever the actual width of the image may be. This package
adds a new keyword rviewport to the graphicx package
specifiying Relative Viewport for graphics inclusion: a window
defined by the given fractions of the natural width and height
of the image.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rviewport/rviewport.sty
%doc %{_texmfdistdir}/doc/latex/rviewport/Makefile
%doc %{_texmfdistdir}/doc/latex/rviewport/README
%doc %{_texmfdistdir}/doc/latex/rviewport/rviewport.pdf
%doc %{_texmfdistdir}/doc/latex/rviewport/vitruvian.jpg
#- source
%doc %{_texmfdistdir}/source/latex/rviewport/rviewport.dtx
%doc %{_texmfdistdir}/source/latex/rviewport/rviewport.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
