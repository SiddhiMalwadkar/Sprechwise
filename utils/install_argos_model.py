import argostranslate.package
import argostranslate.translate

# Download and install English → German model
package_path = argostranslate.package.download_from_url(
    "https://www.argosopentech.com/argospm/index/?from_code=en&to_code=de"
)
argostranslate.package.install_from_path(package_path)

print("EN↔DE model installed successfully!")
