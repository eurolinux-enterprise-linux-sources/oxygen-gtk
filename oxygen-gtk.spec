
Name:    oxygen-gtk
Summary: Oxygen GTK theme
Version: 1.2.0
Release: 5%{?dist}

License: LGPLv2+
Group:   User Interface/Desktops
URL:     https://projects.kde.org/projects/playground/artwork/oxygen-gtk

Requires: oxygen-gtk2
Requires: oxygen-gtk3

BuildArch: noarch

%description
Metapackage for Oxygen GTK+2 and GTK+3 themes.


%prep
# blank

%build
# blank

%install
# blank

%files
# blank

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-2
- metapckage for both GTK+2 and GTK+3 themes

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-1
- oxygen-gtk2-1.2.0
- License: LGPLv2+

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Fri Nov 18 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.5-1
- 1.1.5

* Fri Oct 28 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-3
- disable forcing KDE icons and fonts

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for glibc bug#747377

* Sun Oct 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.4-1
- 1.1.4

* Mon Oct  3 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-3
- fix mozilla applications detection kde#283251

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-2
- BR: dbus-glib-devel

* Fri Sep 16 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Sat Aug 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.2-1
- 1.1.2

* Fri Jul 15 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Tue Jun 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- 1.1.0

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- 1.0.5

* Tue Apr 12 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- 1.0.4

* Mon Mar 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-1
- 1.0.3

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-1
- 1.0.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- oxygen-gtk-1.0.1

* Mon Jan 03 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2
- drop extraneous BR: cairo-devel

* Sun Dec 12 2010 Rex Dieter <rdieter@fedoraproject.org> -  1.0.0-1
- first try




