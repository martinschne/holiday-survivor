import json
import os


class JSONStorage:
    """
    A class to handle JSON-based storage operations.

    This class provides methods to create, read, update, and delete entries in a JSON file.
    It also allows retrieving all stored key-value pairs.
    """

    def __init__(self, file_path):
        """
        Initialize a new JSONStorage object.

        :param file_path: The path to the JSON file to store the data in.
        :type file_path: str
        """
        self.file_path = file_path
        # Ensure the file exists
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)  # Start with an empty dictionary

    def _load(self) -> dict:
        """
        Load the data from the JSON file.

        :returns: The data loaded from the JSON file as a dictionary.
        :rtype: dict
        """
        # Open the JSON file in read mode
        with open(self.file_path, "r") as f:
            # Load and return the data as a dictionary
            return json.load(f)

    def save(self, data: dict) -> None:
        """
        Save the data to the JSON file.

        This method takes a dictionary as input and overwrites the existing
        data in the JSON file with it.
        """
        # Open the JSON file in write mode
        with open(self.file_path, "w") as f:
            # Change the data dictionary to a json string and write it to the json file
            json.dump(data, f, indent=4)

    def create(self, key: str, value: str) -> None:
        """
        Create a new entry in the JSON storage.

        If the key already exists, a ValueError will be raised.
        """
        # Load the current data from the JSON file
        data = self._load()

        # Check if the key exists in the data
        if key in data:
            # Raise an error if the key is not found
            raise ValueError(f"Key '{key}' already exists.")
        # Create a new entry
        data[key] = value
        # Save the changes to the JSON file
        self.save(data)

    def read(self, key: str) -> str:
        """
        Read a value by key from the JSON storage.

        :param key: The key whose value needs to be read.
        :type key: str
        :returns: The value associated with the specified key.
        :raises KeyError: If the key is not found in the storage.
        """
        # Load the current data from the JSON file
        data = self._load()

        # Check if the key exists in the data
        if key not in data:
            # Raise an error if the key is not found
            raise KeyError(f"Key '{key}' not found.")

        # Return the value associated with the key
        return data[key]

    def update(self, key: str, value: str) -> None:
        """
        Update the value of an existing key in the JSON storage.

        :param key: The key whose value needs to be updated.
        :type key: str
        :param value: The new value to be associated with the key.
        :type value: Any
        :raises KeyError: If the key is not found in the storage.
        """
        # Load the current data from the JSON file
        data = self._load()

        # Check if the key exists in the data
        if key not in data:
            # Raise an error if the key is not found
            raise KeyError(f"Key '{key}' not found.")

        # Update the value associated with the key
        data[key] = value

        # Save the updated data back to the JSON file
        self.save(data)

    def delete(self, key: str) -> None:
        """
        Delete a key from the JSON storage.

        :param key: The key to be deleted from the storage.
        :type key: str
        :raises KeyError: If the key is not found in the storage.
        """
        # Load the current data from the JSON file
        data = self._load()

        # Check if the key exists in the data
        if key not in data:
            # Raise an error if the key is not found
            raise KeyError(f"Key '{key}' not found.")

        # Delete the key, value included, from the data
        del data[key]

        # Save the updated data back to the JSON file
        self.save(data)

    def all(self) -> dict:
        """
        Retrieve all key-value pairs from the JSON storage.

        :returns: A dictionary containing all key-value pairs.
        :rtype: dict
        """
        # Load and return all the data from the JSON file
        return self._load()
