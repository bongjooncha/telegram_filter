import style from "./index.module.css";
import Header from "components/Header";
import MakeFilter from "components/MakeFilter";

function Main() {
  return (
    <div className={style.Main}>
      <Header />
      <div className={style.content}>
        <div className={style.left}>
          <MakeFilter />
        </div>
        <div className={style.right}></div>
      </div>
    </div>
  );
}

export default Main;
