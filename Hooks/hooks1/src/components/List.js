import React from "react";
import styled from "@emotion/styled";

const Ul = styled.ul`
  margin-bottom: 20px;
  padding: 0;
`;

const H2 = styled.h2`
  margin: 0;
  padding-bottom: 10px;
`;

export default ({ title, children }) => {
  return (
    <Ul>
      <H2>{title}</H2>
      {children}
    </Ul>
  );
};
