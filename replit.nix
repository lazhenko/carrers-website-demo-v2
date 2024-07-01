{ pkgs }: {
  deps = [
    pkgs.python-launcher
    pkgs.postgresql
    pkgs.openssl
    pkgs.mailutils
    pkgs.python39Packages.flask
  ];
}