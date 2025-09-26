import { useCallback, useState } from "react";
import { useMutation } from "@tanstack/react-query";

import type { UserLogin } from "../api";
import { useLocalStorage } from "@uidotdev/usehooks";
import { useApi } from "../api/useApi";
import { useNavigate } from "react-router-dom";
import { Field, Fieldset, Input, Label } from "@headlessui/react";
import { Button } from "../design-system/Button";

export default function Login() {
  const [formData, setFormData] = useState<UserLogin>({
    username: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [, setPersistedToken] = useLocalStorage("token", "");
  const api = useApi();
  const navigate = useNavigate();
  const loginMutation = useMutation({
    mutationFn: (loginData: UserLogin) => api.loginUser(loginData),
    onSuccess: (response) => {
      setPersistedToken(response.data);
      navigate("/");
    },
    onError: () => {
      setErrorMessage("Invalid username or password");
    },
  });

  const changeUsername = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({
      ...prev,
      username: e.target.value,
    }));
  };

  const changePassword = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({
      ...prev,
      password: e.target.value,
    }));
  };
  const handleSubmit = useCallback(() => {
    loginMutation.mutate(formData);
  }, [formData, loginMutation]);

  return (
    <>
      <title>Login</title>

      <h1>Login</h1>

      <Fieldset>
        <Field>
          <Label>Username:</Label>
          <Input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={changeUsername}
            required
          />
        </Field>

        <Field>
          <Label>Password:</Label>
          <Input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={changePassword}
            required
          />
        </Field>
      </Fieldset>

      {errorMessage && <p>{errorMessage}</p>}
      <Button onClick={handleSubmit} disabled={loginMutation.isPending}>
        {loginMutation.isPending ? "Logging in..." : "Login"}
      </Button>
    </>
  );
}
