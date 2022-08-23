{ pkgs }:

with pkgs;
let
  pytest-base-url = poetry2nix.mkPoetryApplication rec {
    projectDir = fetchFromGitHub {
      owner = "pytest-dev";
      repo = "pytest-base-url";
      rev = "v2.0.0";
      sha256 = "0fbf5hv8ifyg4acdjclwv86gra1clsd10xmcld1vyycd6mx4pamz";
    };
    python = python3;
  };

  # built by poetry, so lots of library conflicts here
  pytest-burl-path = "${pytest-base-url}/${python3.sitePackages}";

  pytest-playwright = with python3Packages; buildPythonPackage rec {
    version = "0.3.0";
    pname = "pytest-playwright";
    disabled = pythonOlder "3.7";

    src = fetchFromGitHub {
      owner = "microsoft";
      repo = "playwright-pytest";
      rev = "v${version}";
      sha256 = "1m2g9gv2h2gj9qnnjsw453fjsqjaydc6mvpg2q14jj01nk2x0z3w";
    };

    postPatch = ''
      substituteInPlace setup.py \
          --replace 'playwright>=1.18' 'playwright' \
          --replace 'setup_requires=["setuptools_scm"],' ""
      # Replace the functionality of setuptools-scm
      echo 'version = "${version}"' > _repo_version.py
      export PYTHONPATH="''${PYTHONPATH}:${pytest-burl-path}"
    '';

    dontUsePythonCatchConflicts = true;

    propagatedBuildInputs = [
      playwright
      pytest
      python-slugify
    ];
  };
  appPackage = import ./default.nix { inherit pkgs; };
in
mkShell {
  name = "playwright";

  packages = [
    appPackage
    (python3.withPackages (pypkgs: with pypkgs; [
      playwright
      pytest-playwright
    ]))
  ];

  shellHook = ''
    export PYTHONPATH="''${PYTHONPATH}:${pytest-burl-path}"
    export PLAYWRIGHT_BROWSERS_PATH=${python3.pkgs.playwright.browsers-linux}
  '';
}
