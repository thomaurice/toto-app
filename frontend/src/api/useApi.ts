import { useLocalStorage } from "@uidotdev/usehooks";
import { DefaultApiFactory } from "./api";
import { useMemo } from "react";
import axios from "axios";

const instance = axios.create();

const useApi = () => {
  const [token] = useLocalStorage("token", "");

  const axiosInstance = useMemo(() => {
    if (token) {
      instance.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    }
    return instance;
  }, [token]);

  const api = useMemo(
    () =>
      DefaultApiFactory(
        {
          isJsonMime: (mime: string) => mime === "application/json",
        },
        "http://localhost:8000",
        axiosInstance
      ),
    [token, axiosInstance]
  );

  return api;
};

export { useApi };
