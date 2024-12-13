// From https://github.com/vitejs/vite/issues/9061#issuecomment-1203035009
// import Form from "@rjsf/core";
import $Form from "@rjsf/core";
// @ts-ignore
const Form = $Form.default || $Form;

import validator from "@rjsf/validator-ajv8";
import { zodToJsonSchema } from "zod-to-json-schema";

interface FormProps {
  formData: any;
  scheme: any;
  name: string;
  method?: "GET" | "POST";
}

export default function ZodForm({
  formData,
  scheme,
  name,
  method = "POST",
}: FormProps) {
  const jsonScheme = zodToJsonSchema(scheme, name);
  return (
    <Form
      method={method}
      schema={jsonScheme}
      validator={validator}
      formData={formData}
      idPrefix={""}
      idSeparator={""}
    />
  );
}
