{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.11";
  };

  outputs = { self, nixpkgs, ... } @ inputs:
    let
      systems = [ "x86_64-linux" "i686-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = f: builtins.listToAttrs (map (name: { inherit name; value = f name; }) systems);
    in
    {
      devShells = forAllSystems (system:
        let pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        }; in
        {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              (python3.withPackages (p: with p; [
                poetry
                pymongo
                flask
                nltk
                pandas
              ]))
              docker-compose
              # mongodb-4_4
            ];
          };
        });
    };
}
