import React from "react";
import styled from "@emotion/styled";
import { keyframes } from "@emotion/react";

const Wrapper = styled.div`
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  width: 100vw;
  height: 100%;
  background-color: #f0f1f3;
  color: #2f3640;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: absolute;
  top: 0;
`;
const Div = styled.div`
  width: 90vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  & > * {
    margin: 0;
    padding: 0;
  }
  @media (max-width: 768px) {
    width: 100vw;
  }
`;

const focus = keyframes`
 0% {
  letter-spacing: -0.5em;
  filter: blur(12px);
  opacity: 0;
}
100% {
  filter: blur(0px);
  opacity: 1;
}
`;

const H1 = styled.h1`
  padding: 15px 0 !important;
  color: #86d3dd;
  font-weight: 800;
  font-size: 40px;
  font-style: italic;
  animation: ${focus} 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
  @media (max-width: 414px) {
    margin-bottom: 30px;
  }
`;

export default ({ children }) => {
  return (
    <Wrapper>
      <Div>
        <H1>be productive</H1>
        {children}
      </Div>
    </Wrapper>
  );
};
