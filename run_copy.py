dist_dir = "./dist/"

import shutil, os

def in_path(name):
    return os.path.abspath(
        "../Geyser-roolback-for-mojang-login/bootstrap/" +
        str.lower(name) +
        "/build/libs/Geyser-" +
        name +
        ".jar"
    )

def out_path(name, dist_dir = dist_dir):
    return os.path.abspath(
        dist_dir +
        "Geyser-roolback-for-mojang-login-" +
        name +
        ".jar"
    )

def cp(name):
    shutil.copy(
        in_path(name) ,
        out_path(name)
    )

if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
os.mkdir(dist_dir)


cp("BungeeCord")
cp("Fabric")
cp("Spigot")
cp("Standalone")
cp("Velocity")

if not os.path.exists("./test-Standalone/"):
    os.mkdir("./test-Standalone/")
shutil.copy(
    in_path("Standalone") ,
    out_path("Standalone", "./test-Standalone/")
)

print("OK!")
