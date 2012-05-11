
Name: app-mail-settings
Epoch: 1
Version: 1.1.4
Release: 1%{dist}
Summary: Mail Settings
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-network

%description
The Mail Settings app provides the necessary tools to manage core mail functionality.

%package core
Summary: Mail Settings - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-mail-core
Requires: app-smtp-core >= 1:1.1.3

%description core
The Mail Settings app provides the necessary tools to manage core mail functionality.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/mail_settings
cp -r * %{buildroot}/usr/clearos/apps/mail_settings/


%post
logger -p local6.notice -t installer 'app-mail-settings - installing'

%post core
logger -p local6.notice -t installer 'app-mail-settings-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/mail_settings/deploy/install ] && /usr/clearos/apps/mail_settings/deploy/install
fi

[ -x /usr/clearos/apps/mail_settings/deploy/upgrade ] && /usr/clearos/apps/mail_settings/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-mail-settings - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-mail-settings-core - uninstalling'
    [ -x /usr/clearos/apps/mail_settings/deploy/uninstall ] && /usr/clearos/apps/mail_settings/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/mail_settings/controllers
/usr/clearos/apps/mail_settings/htdocs
/usr/clearos/apps/mail_settings/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/mail_settings/packaging
%exclude /usr/clearos/apps/mail_settings/tests
%dir /usr/clearos/apps/mail_settings
/usr/clearos/apps/mail_settings/deploy
/usr/clearos/apps/mail_settings/language
/usr/clearos/apps/mail_settings/libraries
