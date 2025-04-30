import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0]))
sys.path.append(str(Path(__file__).resolve().parents[1]))
sys.path.append(str(Path(__file__).resolve().parents[2]))
sys.path.append(str(Path(__file__).resolve().parents[3]))
sys.path.append(str(Path(__file__).resolve().parents[4]))
sys.path.append(str(Path(__file__).resolve().parents[5]))

from vicmil_pip.packages.pyMkDocs import *

pip_manager = PipManager()
pip_manager.add_pip_package("mkdocs")
pip_manager.add_pip_package("mkdocs-material")
pip_manager.add_pip_package("pymdown-extensions")
pip_manager.add_pip_package("mkdocs-monorepo-plugin")

pip_manager.install_missing_modules()

docs_path = get_directory_path(__file__) + "/docs_all"
mono_repo_generator = VmDocsMonoRepoGenerator(docs_path)

# Add all valid mkdocs projects for all packages to docs generator

vicmil_pip_packages = list_installed_vicmil_packages()
print(vicmil_pip_packages)

for package_name in vicmil_pip_packages:
    project_docs_path = f'{get_directory_path(__file__, 1)}/{package_name}/docs'
    if is_mkdocs_project(project_docs_path):
        print(f"adding {package_name} with docs path {project_docs_path}")
        mono_repo_generator.add_project(doc_path=project_docs_path, project_name=package_name)

# Compile all package documentation into a single large documentation page, and show the result in the browser
print(mono_repo_generator.docs_dir)
print(mono_repo_generator._added_projects)
mono_repo_generator.generate()

