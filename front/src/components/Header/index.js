import style from "./header.module.css";
import telegramImg from "assets/images/telegram.png";

function Header() {
  return (
    <div className={style.header}>
      <div className={style.circle}>
        <img src={telegramImg} alt="telegram" className={style.circleImg} />
      </div>
      <span className={style.text}>Telegram Filter</span>
    </div>
  );
}

export default Header;
