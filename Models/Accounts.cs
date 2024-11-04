using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

public class Accounts {
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int HireeID { //if called Id or AccountsId, we would not need [Key]
        get;
        set;
    }
    [Required]
    [MaxLength(255)]
    public string? Username {
        get;
        set;
    }
    [Required]
    [MaxLength(255)]
    public string? Email {
        get;
        set;
    }
    [Required]
    public string? PasswordHash {
        get;
        set;
    }
}