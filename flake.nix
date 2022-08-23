{
  description = "example-heroku-flask-selenium dev shell";

  inputs.nixpkgs.url = "github:yrd/nixpkgs/dc5c9bca2e95424dd391c05515723f2bbf37104e";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (
      system:
        let 
          pkgs = nixpkgs.legacyPackages.${system};
        in
          {
            devShells.default = import ./shell.nix { inherit pkgs; };
            defaultPackage = import ./default.nix { inherit pkgs; };
          }
      );
}
